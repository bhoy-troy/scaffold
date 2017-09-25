import logging

from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_change

from account.views import SettingsView, LoginView
from account.models import Account, EmailAddress

from .forms import CustomLoginForm

log = logging.getLogger(__name__)


class CustomLoginView(LoginView):


    form_class = CustomLoginForm
