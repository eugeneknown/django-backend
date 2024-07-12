from backend.globalFunctions import *
from entity.models import Entities
from hr.models import Schedule

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'schedule'


def define(data):
    model = Schedule()

    if 'id' in data:
        model = Schedule.objects.get(id=data['id'])

    if 'entity_id' in data: model.entity = Entities.objects.get(id=int(data['entity_id']))
    model.schedule_name = data['schedule_name']
    model.monthly_hours = data['monthly_hours']
    model.break_duration = data['break_duration']
    model.schedule_type = data['schedule_type']
    model.work_type = data['work_type']
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = Schedule.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR))
   
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['entity_data'] = model_to_dict(item.entity)
        if 'relations' in data:
            if 'schedule_details' in data['relations']:
                _range = 0
                _value = dict()
                for _item in item.scheduleDetails.exclude(deleted_at__isnull=False).order_by('priority').all():
                    _value[_range] = model_to_dict(_item)
                    _range+=1

                value['schedule_details_data'] = _value

        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = Schedule.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()