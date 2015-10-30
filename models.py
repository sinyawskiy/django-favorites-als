#encoding=utf-8

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

if hasattr(settings, 'AUTH_USER_MODEL'):
    User = settings.AUTH_USER_MODEL
else:
    from django.contrib.auth.models import User


class FavoriteManager(models.Manager):
 
    def create_favorite(self, user, obj):
        """create Favorite for obj and user.
        """
        if not isinstance(obj, models.Model):
            raise ValueError('value must be a Model object')

        content_type = ContentType.objects.get_for_model(type(obj))
        favorite = Favorite(user=user, content_type=content_type,
                            object_id=obj.pk, content_object=obj)
        favorite.save()
        return favorite

    def del_favorite(self, user, obj):
        """del user's Favorite for obj.
        """
        if not isinstance(obj, models.Model):
            raise ValueError('value must be a Model object')

        content_type = ContentType.objects.get_for_model(type(obj))
        self.get_queryset().filter(user=user, content_type=content_type, object_id=obj.pk).delete()

    def favorites_obj_of_user(self, user, model_class):
        """get user's obj. It can tell whether user has favorite obj
        """
        if not isinstance(model_class, models.base.ModelBase):
            raise ValueError('value must be a Model class')

        content_type = ContentType.objects.get_for_model(model_class)
        return self.get_queryset().filter(user=user, content_type=content_type)

    def favorites_for_obj(self, model_class):
        """get favorites for specific object.
        """
        if not isinstance(model_class, models.base.ModelBase):
            raise ValueError('value must be a Model class')

        content_type = ContentType.objects.get_for_model(model_class)
        return self.get_queryset().filter(content_type=content_type)

    def favorites_of_user(self, user):
        """get user's favorites item
        """
        return self.get_queryset().filter(user=user)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created_time = models.DateTimeField(auto_now_add=True)

    objects = FavoriteManager()

    class Meta:
        verbose_name = _('favorite')
        verbose_name_plural = _('favorites')
        unique_together = (('user', 'content_type', 'object_id'),)
        index_together = (('content_type', 'object_id'),)

    def __unicode__(self):
        return "%s likes %s" % (self.user, self.content_object)
