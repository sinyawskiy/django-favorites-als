# -*- coding: utf-8 -*-
from django.views.generic import View
from annoying.responses import JSONResponse
from testapp.models import TestModel
from favorites.models import Favorite


class TestFavoritesView(View):
    def get(self, request, uuid):
        if request.user.is_authenticated() and request.user.has_perm('testapp.test_add_to_favorites'):
            errors = []
            action = u''
            try:
                person = Person.objects.get(uuid=uuid)
            except Person.DoesNotExist:
                errors.append(u'Персона не найдена')
            else:
                favorites = Favorite.objects.favorites_obj_of_user(request.user, person)
                if person in [favorite.content_object for favorite in favorites]:
                    Favorite.objects.del_favorite(request.user, person)
                    action = u'del'
                else:
                    Favorite.objects.create_favorite(request.user, person)
                    action = u'add'

            return JSONResponse({
                'success': len(errors) == 0,
                'errors': errors,
                'action': action
            })
