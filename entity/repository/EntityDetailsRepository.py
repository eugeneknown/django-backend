from backend.globalFunctions import *
from entity.models import EntityDetails
from hr.models import CareerPlatforms

from django.utils import timezone

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status


meta_data = 'entity_details'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")

def define(data):
    model = EntityDetails()

    if 'id' in data:
        model = EntityDetails.objects.get(id=data['id'])
    else:
        model = CareerPlatforms.objects.get(id=data['platforms_id'])

    model.salaru = data['salaru']
    model.us_time = data['us_time']
    model.work_in_office = data['work_in_office']
    model.transpo = data['transpo']
    model.application = data['application']
    model.start = data['start']
    model.condition = data['condition']
    model.part_time = data['part_time']

    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = EntityDetails.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    if 'order' in data: object = object.order_by('-'+data['order']['target'] if data['order']['value'] == 'desc' else data['order']['target'])

    if 'relations' in data:
        range = 0
        for item in object:
            value =  model_to_dict(item)
            if 'entity' in data['relations']:
                if item.entity is not None: value['entity_data'] = model_to_dict(item.entity)

            if 'platforms' in data['relations']:
                if item.platforms is not None: value['platforms_data'] = model_to_dict(item.platforms)
        
            result[range] = value
            range+=1

    else:
        result = object.values() 


    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = EntityDetails.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = EntityDetails.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)