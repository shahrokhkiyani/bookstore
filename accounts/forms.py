from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# TODO: User Creation Form
# TODO: User Change Form


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
