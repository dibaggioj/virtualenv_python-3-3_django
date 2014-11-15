from django import forms
from photos.models import UploadPhoto


class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = UploadPhoto