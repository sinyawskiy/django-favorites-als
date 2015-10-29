# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import never_cache
from favorites.views import TestFavoritesView


urlpatterns = patterns('',
    url(r'^favorites/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', never_cache(TestFavoritesView.as_view()), name='test_favorites'),
)
