from backend.globalFunctions import *
from entity.models import Experience
from entity.models import ExperienceDetails

from django.utils import timezone

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status


meta_data = 'experience_details'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")

def define(data):
    model = ExperienceDetails()

    if 'id' in data:
        model = ExperienceDetails.objects.get(id=data['id'])
    else:
        model.experience = Experience.objects.get(id=data['experience_id'])

    model.company = data['company']
    model.department = data['department']
    model.position_held = data['position_held']
    model.start_date = data['start_date']
    model.end_date = data['end_date']
    model.handled = data['handled']
    model.stay_length = data['stay_length']
    model.leave_reason = data['leave_reason']
    model.salary = data['salary']
    if 'present' in data: model.present = data['present']
    model.order = data['order']

    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = ExperienceDetails.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    if 'order' in data: object = object.order_by('-'+data['order']['target'] if data['order']['value'] == 'desc' else data['order']['target'])

    result = object.values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = ExperienceDetails.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = ExperienceDetails.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)