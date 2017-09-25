# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.functional import curry
from django.views.defaults import page_not_found, server_error

from django_scaffold.views import Index

admin.autodiscover()

urlpatterns = [
# url(r'^admin/login/', LoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url(r'^profile/$', Index.as_view()),
    url(r"^account/", include("account.urls")),
    url(r"^api/", include("api.urls", namespace='api') ),
    url(r'^hijack/', include('hijack.urls')),
    # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = curry(page_not_found, template_name='404.html')
handler500 = curry(server_error, template_name='500.html')


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns