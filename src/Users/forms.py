from django import forms
from .models import Location
from localflavor.us.forms import USZipCodeField

class LocationForm(forms.ModelForm):

    Address_1 = forms.CharField(required=True)
    Zip_Code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = {'Address_1', 'Address_2', 'City', 'State', 'Zip_Code'}