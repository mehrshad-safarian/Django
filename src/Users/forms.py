from django import forms
from localflavor.us.forms import USZipCodeField
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .models import Location, Profile
from .widgets import CustomPictureImageFieldWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget, required=False)
    bio = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout('bio', 'phone_number')

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        # if clear checkbox is checked, allow None
        if not photo and self.initial.get('photo'):
            if self.data.get('photo-clear'):
                return None
            # no new file and no clear = keep existing photo
            return self.initial.get('photo')
        return photo

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    Address_1 = forms.CharField(required=True)
    Zip_Code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = {'Address_1', 'Address_2', 'City', 'State', 'Zip_Code'}