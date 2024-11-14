from backend.globalFunctions import *
from entity.models import Entities
from entity.models import EntityReference

from django.utils import timezone

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status


meta_data = 'entity_reference'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")

def define(data):
    model = EntityReference()

    if 'id' in data:
        model = EntityReference.objects.get(id=data['id'])
    else:
        model.entity = Entities.objects.get(id=data['entity_id'])

    model.name = data['name']
    model.position = data['position']
    model.email = data['email']
    model.contact_number = data['contact_number']
    model.company = data['company']
    model.company_email = data['company_email']

    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = EntityReference.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    if 'order' in data: object = object.order_by('-'+data['order']['target'] if data['order']['value'] == 'desc' else data['order']['target'])

    result = object.values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = EntityReference.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = EntityReference.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)