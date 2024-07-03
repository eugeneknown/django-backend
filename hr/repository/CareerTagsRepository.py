from backend.globalFunctions import *
from hr.models import CareerTags

from rest_framework.response import Response
from rest_framework import status

from django.forms.models import model_to_dict
from django.db.models import Q, Count

from datetime import datetime


meta_data = 'career_tags'
now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")


def define(data):
    model = CareerTags()

    if 'id' in data:
        model = CareerTags.objects.get('data')

    model.title = data['title']
    model.color = data['color']
    
    now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    filter = genericModelFilter(data)
    result = CareerTags.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR)).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = CareerTags.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = CareerTags.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)