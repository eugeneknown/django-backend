from backend.globalFunctions import *
from hr.models import TimeSheets, TimeSheetDetails, Schedule, ScheduleDetails 

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'timesheet_details'


def define(data):
    model = TimeSheetDetails()

    if 'id' in data:
        model = TimeSheetDetails.objects.get(id=data['id'])

    if 'timesheet_id' in data: model.timesheet = TimeSheets.objects.get(id=int(data['timesheet_id']))
    if 'schedule_id' in data: model.schedule = Schedule.objects.get(id=int(data['schedule_id']))
    if 'schedule_details_id' in data: model.schedule_detials = ScheduleDetails.objects.get(id=int(data['schedule_details_id']))
    model.log_start = data['log_start'] if 'log_start' in data else None
    model.log_end = data['lgo_end'] if 'lgo_end' in data else None
    model.schedule_type = data['schedule_type']
    model.schedule_status = data['schedule_status']
    model.actual_start = data['actual_start']
    model.actual_end = data['actual_end']
    model.approved_start = data['approved_start']
    model.approved_end = data['approved_end']
    model.total_hours = data['total_hours']
    model.confirmed_hours = data['confirmed_hours']
    model.confirmation_type = data['confirmation_type']
    model.remarks = data['remarks']
    model.status = data['status'] if 'status' in data else 'pending'
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = TimeSheetDetails.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR))
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['timesheet_data'] = model_to_dict(item.timesheet)
        value['schedule_data'] = model_to_dict(item.schedule)
        value['schedule_details_data'] = model_to_dict(item.schedule_detials)
        value['log_start_data'] = model_to_dict(item.log_start)
        value['log_end_data'] = model_to_dict(item.log_end)
        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = TimeSheetDetails.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()