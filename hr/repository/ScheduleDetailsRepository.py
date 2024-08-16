from backend.globalFunctions import *
from hr.models import Schedule, ScheduleDetails

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'schedule_details'


def define(data):
    model = ScheduleDetails()

    if 'id' in data:
        model = ScheduleDetails.objects.get(id=data['id'])

    if 'schedule_id' in data: model.schedule = Schedule.objects.get(id=int(data['schedule_id']))
    model.time_start = data['time_start']
    model.time_end = data['time_end']
    model.duration = data['duration']
    model.repeat = data['repeat']
    model.days = data['days']
    model.priority = data['priority']
    model.amount = data['amount']
    model.amount_type = data['amount_type']
    model.other_type = data['other_type']
    model.in_threshold = data['in_threshold']
    model.out_threshold = data['out_threshold']
    model.is_expandable = data['is_expandable']
    model.must_check_in = data['must_check_in']
    model.must_check_out = data['must_check_out']
    model.timezone = data['timezone']
    model.multi_day = data['multi_day']
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = ScheduleDetails.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
   
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['schedule_data'] = model_to_dict(item.schedule)
        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = ScheduleDetails.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()