# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import routers
from django.conf.urls import  url
from .views import UserViewSet

__all__ = ['urls']

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


def urls():
    return router.urls

