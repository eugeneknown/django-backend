from backend.globalFunctions import *
from entity.models import Experience 
from entity.models import Entities
from entity.models import ExperienceDetails

from django.utils import timezone

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F, Prefetch
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status


meta_data = 'experience'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")

def define(data):
    model = Experience()

    if 'id' in data:
        model = Experience.objects.get(id=data['id'])
    else:
        model.entity = Entities.objects.get(id=data['entity_id'])

    model.total_experience = data['total_experience']
    model.other_experience = data['other_experience']

    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = Experience.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
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
    result = Experience.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = Experience.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)