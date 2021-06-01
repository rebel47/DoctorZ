from django import forms
from django.contrib.auth.models import User

class editProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

    # def __init__(self, *args, **kwargs):
    #     super(editProfile, self).__init__(*args, **kwargs)