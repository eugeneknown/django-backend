from backend.globalFunctions import *
from hr.models import TimeSheets
from entity.models import Entities

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'timesheet'


def define(data):
    model = TimeSheets()

    if 'id' in data:
        model = TimeSheets.objects.get(id=data['id'])

    if 'entity_id' in data: model.entity = Entities.objects.get(id=int(data['entity_id']))
    model.year = data['year']
    model.month = data['month']
    model.period_start = data['period_start']
    model.period_end = data['period_end']
    model.scheduled_days = data['scheduled_days']
    model.scheduled_hours = data['scheduled_hours']
    model.actual_days = data['actual_days']
    model.actual_hours = data['actual_hours']
    model.approved_days = data['approved_days']
    model.approved_hours = data['approved_hours']
    model.remarks = data['remarks']
    # model.prepared_by = data['prepared_by']
    # model.approved_by = data['approved_by']
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    # print(filter)
    object = TimeSheets.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR))
    # print(object.query)
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['entity_data'] = model_to_dict(item.entity)
        result[range] = value
        range+=1

    # print(result)
    return Response({meta_data: result}, status=status.HTTP_200_OK)

# all({
#     'filter': [
#         {
#             'target': 'created_at',
#             'operator': 'range',
#             'value': ['2024-03-05', '2024-03-08 23:59:59'],
#         },
#     ],
# })

def fetch(data, id):
    result = TimeSheets.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()


# def timesheetGenerate():
    