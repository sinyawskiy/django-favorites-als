# -*- coding: utf-8 -*-
from django.views.generic import View
from annoying.responses import JSONResponse
from communications.models import PersonCommunication
from contacts.models import Person
from favorites.models import Favorite
from hierarchy.models import Company


class PersonFavoritesView(View):
    def get(self, request, uuid):
        if request.user.is_authenticated() and request.user.has_perm('contacts.person_add_to_favorites'):
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


class CompanyFavoritesView(View):
    def get(self, request, uuid):
        if request.user.is_authenticated() and request.user.has_perm('hierarchy.company_add_to_favorites'):
            errors = []
            action = u''
            try:
                company = Company.objects.get(uuid=uuid)
            except Company.DoesNotExist:
                errors.append(u'Компания не найдена')
            else:
                favorites = Favorite.objects.favorites_obj_of_user(request.user, company)
                if company in [favorite.content_object for favorite in favorites]:
                    Favorite.objects.del_favorite(request.user, company)
                    action = u'del'
                else:
                    Favorite.objects.create_favorite(request.user, company)
                    action = u'add'
            return JSONResponse({
                'success': len(errors) == 0,
                'errors': errors,
                'action': action
            })


class PersonCommunicationFavoritesView(View):
    def get(self, request, communication_id):
        if request.user.is_authenticated() and request.user.has_perm('communications.person_communication_add_to_favorites'):
            errors = []
            action = u''
            try:
                communication = PersonCommunication.objects.get(id=communication_id)
            except PersonCommunication.DoesNotExist:
                errors.append(u'Средство связи не найдена')
            else:
                favorites = Favorite.objects.favorites_obj_of_user(request.user, communication)
                if communication in [favorite.content_object for favorite in favorites]:
                    Favorite.objects.del_favorite(request.user, communication)
                    action = u'del'
                else:
                    Favorite.objects.create_favorite(request.user, communication)
                    action = u'add'
            return JSONResponse({
                'success': len(errors) == 0,
                'errors': errors,
                'action': action
            })