from backend.globalFunctions import *
from entity.models import Entities 

from django.utils import timezone

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F, Prefetch

from rest_framework.response import Response
from rest_framework import status

from django.core import serializers


meta_data = 'entity'

def define(data):
    model = Entities()

    if 'id' in data:
        #logics
        model = Entities.objects.get(id=data['id'])

    if 'users_id' in data: 
        model = Entities.objects.get(users_id=data['users_id'])

    model.first_name = data['first_name']
    model.last_name = data['last_name']
    model.middle_name = data['middle_name']
    model.full_name = data['first_name'] +" "+ data['last_name']
    model.permanent_address = data['permanent_address']
    model.present_address = data['present_address']
    model.email = data['email']
    model.contact_number = data['contact_number']
    model.birthday = data['birthday']
    model.birth_place = data['birth_place']
    model.civil_status = data['civil_status']
    model.age = data['age']
    model.gender = data['gender']
    model.nickname = data['nickname']
    model.children = data['children']
    model.alternative_number = data['alternative_number']
    model.birth_order = data['birth_order']
    model.education = data['education']
    model.course = data['course']
    model.gender = data['gender']
    model.religion = data['religion']

    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = Entities.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    if 'order' in data: object = object.order_by('-'+data['order']['target'] if data['order']['value'] == 'desc' else data['order']['target'])

    if 'relations' in data:
        if 'details' in data['relations']:
            range = 0
            object = object.prefetch_related('details')
            for item in object:
                value =  model_to_dict(item)

                _range = 0
                _value = dict()
                for _item in item.details.all():
                    _value[_range] = model_to_dict(_item)
                    _range+=1


                value['details'] = _value
                result[range] = value
                range+=1

    else:
        result = object.values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    # model = Entities()

    result = Entities.objects.filter(id=id).values()

    return Response({'entity':result}, status=status.HTTP_200_OK)


def delete():
    #todo
    print()