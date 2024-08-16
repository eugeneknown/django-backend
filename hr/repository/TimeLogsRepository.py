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
    for item in data:
        setattr(model, item, data[item])
        
    # print(model_to_dict(model))
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


# define({
#     'id': 1,
#     'duration': 100
# })


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = TimeLogs.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['entity_data'] = model_to_dict(item.entity)
        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)

# all({
#     'filter': [
#         {
#             'target': 'entity_id',
#             'operator': '=',
#             'value': 1,
#         },
#         {
#             'target': 'log_end',
#             'operator': '<>',
#             'value': True
#         },
#     ],
#     'exclude': [
#         {
#             'target': 'log_start',
#             'operator': '=',
#             'value': None,
#         }
#     ],
# })

def fetch(data, id):
    result = TimeLogs.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()


def lastLogCheck(id):
    result = dict()

    end_log = TimeLogs.objects.filter(
        entity=id,
        log_start__isnull=False,
        log_end__isnull=True,
    ).last()

    if not end_log:
        return Response({meta_data: 'no end log'}, status=status.HTTP_404_NOT_FOUND)

    last_log = TimeLogs.objects.filter(entity=id).last()

    if not last_log:
        return Response({meta_data: 'no last log'}, status=status.HTTP_404_NOT_FOUND)
        
    if end_log.pk is not last_log.pk:
        return Response({meta_data: result}, status=status.HTTP_404_NOT_FOUND)

    result = TimeLogs.objects.filter(id=end_log.pk).values().last()

    return Response({meta_data: result}, status=status.HTTP_200_OK)