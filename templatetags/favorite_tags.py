#encoding=utf-8
from favorites.models import Favorite
from django.db import models
from django import template


register = template.Library()


@register.filter
def favorite_count(value):
    if not isinstance(value, models.base.ModelBase):
        raise ValueError('value must be a Model class')
    count = Favorite.objects.favorites_for_obj(value).count()
    return str(count)


@register.filter
def is_in_favorites(user, favorite_object):
    if not isinstance(favorite_object, models.Model):
        raise ValueError('favorite_object must be a Model object')
    return favorite_object in [
        favorite.content_object for favorite in Favorite.objects.favorites_obj_of_user(user, type(favorite_object))
    ] if user.is_authenticated() else False
