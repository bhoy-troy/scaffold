# Create your views here.
import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from account.models import EmailAddress
from account.forms import SettingsForm, LoginUsernameForm
from account.conf import settings
import pytz

from .models import UserProfile


class CustomLoginForm(LoginUsernameForm):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'placeholder': _('Username'), 'autofocus': 'autofocus'}),
                               localize=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Password')}), localize=True)

