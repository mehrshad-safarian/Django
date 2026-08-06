from importlib import reload
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LikedListing, Listing
from django.contrib import messages

from .forms import ListingForm

from Users.forms import LocationForm
from .filters import ListingFilter

def main_view(request):
    return render(request, 'views/main.html', {'name': 'Tehran Luxury Cars'})


@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    user_liked_listings = LikedListing.objects.filter(
        profile=request.user.profile).values_list('listing')
    liked_listings_ids = [l[0] for l in user_liked_listings]
    context = {
        'listings': listings,
        'listing_filter': listing_filter,
        'liked_listings_ids': liked_listings_ids,
    }
    return render(request, "views/home.html", context)


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form})

@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing,})
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing!')
        return redirect('home')
    
    
@login_required
def edit_view(request, id):
    try:
        # Get the listing object from DB using ID
        listing = Listing.objects.get(id=id)
        # Safety check (redundant, but kept from course style)
        if listing is None:
            raise Exception
        # If user submits the form
        if request.method == 'POST':
            # Bind submitted data to forms
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            # Validate both forms
            if listing_form.is_valid() and location_form.is_valid():
                # Save location first (updates or creates location object)
                location = location_form.save()
                # Save listing but don't commit yet (we need to modify it first)
                listing = listing_form.save(commit=False)
                # IMPORTANT: manually link listing to updated location
                listing.location = location
                # Now save final listing object
                listing.save()
                # Success message
                messages.info(request, f'Listing {id} updated successfully!')
                return redirect('home')
            else:
                # If validation fails, show error and re-render page
                messages.error(request, 'An error occurred while trying to update listings.')
                return render(request, 'views/edit.html', context)
        else:
            # GET request → show form with existing data
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        # Send forms to template
        context = {
            'location_form': location_form,
            'listing_form': listing_form
        }
        return render(request, 'views/edit.html', context)
    except Exception as e:
        # Handle unexpected errors (DB errors, missing listing, etc.)
        messages.error(
            request, 'An error occurred while trying to access the edit page.'
        )
        return redirect('home')


@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)

    liked_listing, created = LikedListing.objects.get_or_create(
        profile=request.user.profile, listing=listing)

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    return JsonResponse({
        'is_liked_by_user': created
    })
