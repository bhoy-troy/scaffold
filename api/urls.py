# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from api import v1

urlpatterns = [
    url(r'^v1/', include(v1.urls(), namespace='v1')),

]




