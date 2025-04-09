from django import forms
from .models import AppVarity

class AppVarityForm(forms.Form):
    app_varity = forms.ModelChoiceField
    (queryset=AppVarity.objects.all(), 
     label = "Select App Varity")
