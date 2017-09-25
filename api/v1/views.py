# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

from rest_framework import authentication, permissions


class UserViewSet(viewsets.ModelViewSet):
    """
      Return a list of all the existing users.
      """

    # authentication_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
