# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import never_cache
from favorites.views import PersonFavoritesView, CompanyFavoritesView, PersonCommunicationFavoritesView


urlpatterns = patterns('',
    url(r'^favorites/person/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', never_cache(PersonFavoritesView.as_view()), name='person_favorites'),
    url(r'^favorites/hierarchy/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', never_cache(CompanyFavoritesView.as_view()), name='company_favorites'),
    url(r'^favorites/person_communication/(?P<communication_id>[1234567890]+)/$', never_cache(PersonCommunicationFavoritesView.as_view()), name='person_communication_favorites'),
)