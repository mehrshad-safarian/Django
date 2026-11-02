from django import forms
from .models import Location, Profile
from localflavor.us.forms import USZipCodeField
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')


class LocationForm(forms.ModelForm):

    Address_1 = forms.CharField(required=True)
    Zip_Code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = {'Address_1', 'Address_2', 'City', 'State', 'Zip_Code'}