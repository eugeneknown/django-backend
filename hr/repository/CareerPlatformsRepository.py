from backend.globalFunctions import *
from hr.models import CareerPlatforms

from rest_framework.response import Response
from rest_framework import status

from django.forms.models import model_to_dict
from django.db.models import Q, Count

from django.utils import timezone


meta_data = 'career_platforms'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")


def define(data):
    model = CareerPlatforms()

    if 'id' in data:
        model = CareerPlatforms.objects.get('data')

    model.title = data['title']
    model.color = data['color']
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    filter = genericModelFilter(data)
    result = CareerPlatforms.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR)).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = CareerPlatforms.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = CareerPlatforms.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)