from django import forms

from .models import profile

class profileForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={'required': 'Please let us know what to call you!'}
    )
    class Meta:
        model = profile
        fields = '__all__'

        labels = {
            "name": "Your name",
            "bio": 'Your description',
        }
        