#encoding=utf-8
from favorites.models import Favorite
from django.db import models
from django import template
register = template.Library()


def favorite_count(value):
    if not isinstance(value, models.Model):
        raise ValueError('value must be a Model object')
    count = Favorite.objects.favorites_for_obj(value).count()
    return str(count)

register.filter('favorite_count', favorite_count)


def is_in_favorites(user, favorite_object):
    return favorite_object in [favorite.content_object for favorite in Favorite.objects.favorites_obj_of_user(user, type(favorite_object))]

register.filter('is_in_favorites', is_in_favorites)
