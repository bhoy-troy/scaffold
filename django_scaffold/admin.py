# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms as auth_forms

from hijack_admin.admin import HijackUserAdminMixin

from user_profile.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdminChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        help_texts = {
            'username': None,
            '_is_active': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserAdminChangeForm, self).__init__(*args, **kwargs)

        # We need to remove the password field because of the the
        # changes to the User model to incorporate Keycloak
        del self.fields['password']


class CustomUserAdmin(UserAdmin, HijackUserAdminMixin):
    inlines = (ProfileInline,)
    search_fields = ('username', 'email')

    form = UserAdminChangeForm
    list_display = ('username', 'email', 'hijack_field')
    fieldsets = (
        ('User Details', {
            'fields': ('username', 'first_name', 'last_name', 'email',
                       'is_active',)
        }),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), CustomUserAdmin)
