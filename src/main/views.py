from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import LikedListing, Listing, ListingInquiry
from .forms import ListingForm
from Users.forms import LocationForm
from .filters import ListingFilter


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
        profile=request.user.profile
    ).values_list('listing')

    liked_listings_ids = [l[0] for l in user_liked_listings]

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

    try:

        listing = Listing.objects.get(
            id=id
        )

        if listing is None:
            raise Exception

        return render(
            request,
            'views/listing.html',
            {
                'listing': listing,
            }
        )

    except Exception:

        messages.error(
            request,
            f'Invalid UID {id} was provided for listing!'
        )

        return redirect('home')


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

        # GET request
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

    # Check if this user has already sent an inquiry
    inquiry, created = ListingInquiry.objects.get_or_create(
        profile=request.user.profile,
        listing=listing
    )

    # User has already sent an email
    if not created:

        return JsonResponse({
            'success': False,
            'already_sent': True,
            'info': 'You have already sent an inquiry for this listing.'
        })

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
            "SEND MAIL RESULT:",
            result
        )

        return JsonResponse({
            'success': True,
            'result': result,
        })

    except Exception as e:

        print(
            "EMAIL ERROR:",
            e
        )

        # Email failed, so allow the user to try again
        inquiry.delete()

        return JsonResponse({
            'success': False,
            'info': str(e),
        })