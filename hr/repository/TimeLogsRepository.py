from backend.globalFunctions import *
from hr.models import TimeLogs
from entity.models import Entities

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'time_logs'


def define(data):
    model = TimeLogs()

    if 'id' in data:
        model = TimeLogs.objects.get(id=data['id'])

    if 'entity_id' in data: model.entity = Entities.objects.get(id=int(data['entity_id']))
    # model.work_area_code = data['work_area_code']
    # model.duration = data['duration']
    # model.log_start = data['log_start']
    # model.log_end = data['log_end']
    # model.log_start = data['log_start']
    # model.log_status = data['log_status']
    # model.timezone = data['timezone']
    # model.remarks = data['remarks']

    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    # model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = TimeLogs.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR))
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['entity_data'] = model_to_dict(item.entity)
        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = TimeLogs.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()