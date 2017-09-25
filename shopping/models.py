# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


from django.db import models
from django.conf import settings

# Create your models here.


class ShoppingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = _("Shopping List")
        verbose_name_plural = _("Shopping Lists")


class ShoppingItem(models.Model):
    item = models.CharField(blank=False, null=False, max_length=255)
    notes = models.TextField(blank=True)
    list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)


