# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.contrib.sitemaps.views import sitemap


admin.autodiscover()

admin.site.site_header = 'Studio REC'
admin.site.site_title = 'Studio REC'
admin.site.index_title = 'Administración del contenido del sitio Studio REC'

urlpatterns = [
    url(r'^select2/', include('django_select2.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}},
        name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('djangocms_forms.urls')),
    url(r'^', include('cms.urls')),
    prefix_default_language=False
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
