from backend.globalFunctions import *

from files.models import Files, EntityHasFiles
from entity.models import Entities

from rest_framework.response import Response
from rest_framework import status

from django.forms.models import model_to_dict
from django.db.models import Q

from django.utils import timezone


meta_data = 'entity_files'

def define(data):
    model = EntityHasFiles()

    if 'id' in data:
        model = EntityHasFiles.objects.get(id=data['id'])
    else:
        model.entity = Entities.objects.get(id=data['entity_id'])
        model.files = Files.objects.get(id=data['files_id'])

    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    filter = genericModelFilter(data)
    result = EntityHasFiles.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR)).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = EntityHasFiles.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()