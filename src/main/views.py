from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import LikedListing, Listing, ListingInquiry, ListingInquiryAttempt
from .forms import ListingForm
from Users.forms import LocationForm
from .filters import ListingFilter

from datetime import timedelta
from django.utils import timezone

def main_view(request):
    return render(
        request,
        'views/main.html',
        {'name': 'Tehran Luxury Cars'}
    )


@login_required
def home_view(request):
    listings = Listing.objects.all()

    listing_filter = ListingFilter(
        request.GET,
        queryset=listings
    )

    user_liked_listings = LikedListing.objects.filter(
        profile__user=request.user
    ).values_list('listing_id', flat=True)

    liked_listings_ids = list(user_liked_listings)

    context = {
        'listings': listings,
        'listing_filter': listing_filter,
        'liked_listings_ids': liked_listings_ids,
    }

    return render(
        request,
        "views/home.html",
        context
    )


@login_required
def list_view(request):

    if request.method == 'POST':

        try:

            listing_form = ListingForm(
                request.POST,
                request.FILES
            )

            location_form = LocationForm(
                request.POST
            )

            if listing_form.is_valid() and location_form.is_valid():

                listing = listing_form.save(
                    commit=False
                )

                listing_location = location_form.save()

                listing.seller = request.user.profile
                listing.location = listing_location

                listing.save()

                messages.info(
                    request,
                    f'{listing.model} Listing Posted Successfully!'
                )

                return redirect('home')

            else:
                raise Exception()

        except Exception as e:

            print(e)

            messages.error(
                request,
                'An error occured while posting the listing.'
            )

    elif request.method == 'GET':

        listing_form = ListingForm()
        location_form = LocationForm()

    return render(
        request,
        'views/list.html',
        {
            'listing_form': listing_form,
            'location_form': location_form
        }
    )


@login_required
def listing_view(request, id):

    listing = get_object_or_404(
        Listing,
        id=id
    )

    inquiry = ListingInquiry.objects.filter(
        profile=request.user.profile,
        listing=listing
    ).first()

    email_sent_count = 0

    if inquiry:
        email_sent_count = inquiry.attempts.count()

    return render(
        request,
        'views/listing.html',
        {
            'listing': listing,
            'email_sent_count': email_sent_count,
            'has_inquiry': inquiry is not None,
        }
    )


@login_required
def edit_view(request, id):

    try:

        # Get the listing object from DB
        listing = Listing.objects.get(
            id=id
        )

        if listing is None:
            raise Exception

        # POST request
        if request.method == 'POST':

            listing_form = ListingForm(
                request.POST,
                request.FILES,
                instance=listing
            )

            location_form = LocationForm(
                request.POST,
                instance=listing.location
            )

            if listing_form.is_valid() and location_form.is_valid():

                # Save location
                location = location_form.save()

                # Save listing without committing
                listing = listing_form.save(
                    commit=False
                )

                # Link updated location
                listing.location = location

                listing.save()

                messages.info(
                    request,
                    f'Listing {id} updated successfully!'
                )

                return redirect('home')

            else:

                messages.error(
                    request,
                    'An error occurred while trying to update listings.'
                )

                context = {
                    'location_form': location_form,
                    'listing_form': listing_form
                }

                return render(
                    request,
                    'views/edit.html',
                    context
                )

        else:

            listing_form = ListingForm(
                instance=listing
            )

            location_form = LocationForm(
                instance=listing.location
            )

            context = {
                'location_form': location_form,
                'listing_form': listing_form
            }

            return render(
                request,
                'views/edit.html',
                context
            )

    except Exception as e:

        print(e)

        messages.error(
            request,
            'An error occurred while trying to access the edit page.'
        )

        return redirect('home')


@login_required
def like_listing_view(request, id):

    listing = get_object_or_404(
        Listing,
        id=id
    )

    liked_listing, created = LikedListing.objects.get_or_create(
        profile=request.user.profile,
        listing=listing
    )

    if not created:
        liked_listing.delete()

    else:
        liked_listing.save()

    return JsonResponse({
        'is_liked_by_user': created
    })


@login_required
def inquire_listing_using_email(request, id):

    listing = get_object_or_404(
        Listing,
        id=id
    )

    profile = request.user.profile
    if not listing.seller.user.email:
        return JsonResponse({
            'success': False,
            'info': 'The seller has no email address.'
        }, status=400)
    

    # Inquiry limits
    DAILY_LIMIT = 2
    WEEKLY_LIMIT = 5
    LISTING_LIMIT = 10

    # Count user's successful emails today
    today = timezone.localdate()

    daily_sent_count = ListingInquiryAttempt.objects.filter(
        inquiry__profile=profile,
        sent_at__date=today
    ).count()

    # Count user's successful emails this week
    week_start = today - timedelta(
        days=today.weekday()
    )

    weekly_sent_count = ListingInquiryAttempt.objects.filter(
        inquiry__profile=profile,
        sent_at__date__gte=week_start
    ).count()

    # Count successful emails for this listing
    listing_sent_count = ListingInquiryAttempt.objects.filter(
        inquiry__listing=listing
    ).count()

    # Daily limit
    if daily_sent_count >= DAILY_LIMIT:

        return JsonResponse({
            'success': False,
            'limit_reached': True,
            'limit_type': 'daily',
            'info': 'You have reached your daily email limit.',
            'sent_count': listing_sent_count,
            'daily_remaining': 0,
            'weekly_remaining': max(
                WEEKLY_LIMIT - weekly_sent_count,
                0
            ),
            'listing_remaining': max(
                LISTING_LIMIT - listing_sent_count,
                0
            ),
        }, status=429)

    # Weekly limit
    if weekly_sent_count >= WEEKLY_LIMIT:

        return JsonResponse({
            'success': False,
            'limit_reached': True,
            'limit_type': 'weekly',
            'info': 'You have reached your weekly email limit.',
            'sent_count': listing_sent_count,
            'daily_remaining': max(
                DAILY_LIMIT - daily_sent_count,
                0
            ),
            'weekly_remaining': 0,
            'listing_remaining': max(
                LISTING_LIMIT - listing_sent_count,
                0
            ),
        }, status=429)

    # Listing limit
    if listing_sent_count >= LISTING_LIMIT:

        return JsonResponse({
            'success': False,
            'limit_reached': True,
            'limit_type': 'listing',
            'info': 'This listing has reached its email limit.',
            'sent_count': listing_sent_count,
            'daily_remaining': max(
                DAILY_LIMIT - daily_sent_count,
                0
            ),
            'weekly_remaining': max(
                WEEKLY_LIMIT - weekly_sent_count,
                0
            ),
            'listing_remaining': 0,
        }, status=429)

    try:

        emailSubject = (
            f'{request.user.username} is interested in {listing.model}'
        )

        emailMessage = (
            f'Hi {listing.seller.user.username}, '
            f'{request.user.username} is interested in your '
            f'{listing.model} listing on TLC'
        )

        result = send_mail(
            emailSubject,
            emailMessage,
            settings.DEFAULT_FROM_EMAIL,
            [listing.seller.user.email],
            fail_silently=False,
        )

        print(
            'SEND MAIL RESULT:',
            result
        )

        # Email was not sent
        if result != 1:

            return JsonResponse({
                'success': False,
                'info': 'The email could not be sent.'
            }, status=500)

        # Create the inquiry on the first successful email
        inquiry, created = ListingInquiry.objects.get_or_create(
            profile=profile,
            listing=listing
        )

        # Record the successful email attempt
        ListingInquiryAttempt.objects.create(
            inquiry=inquiry
        )

        # Update counts after successful email
        daily_sent_count += 1
        weekly_sent_count += 1
        listing_sent_count += 1

        return JsonResponse({
            'success': True,
            'already_sent': not created,
            'sent_count': listing_sent_count,
            'daily_remaining': max(
                DAILY_LIMIT - daily_sent_count,
                0
            ),
            'weekly_remaining': max(
                WEEKLY_LIMIT - weekly_sent_count,
                0
            ),
            'listing_remaining': max(
                LISTING_LIMIT - listing_sent_count,
                0
            ),
        })

    except Exception as e:

        print(
            'EMAIL ERROR:',
            e
        )

        return JsonResponse({
            'success': False,
            'info': str(e),
        }, status=500)