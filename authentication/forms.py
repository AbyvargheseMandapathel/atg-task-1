from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# user_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'email', 'profile_picture', 'address_line1', 'address_city', 'address_state', 'address_pincode', 'first_name', 'last_name'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


