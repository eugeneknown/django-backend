from entity.models import Entities 

from django.utils import timezone

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status

from django.core import serializers


meta_data = 'entity'

def define(data):
    model = Entities()

    if 'id' in data:
        #logics
        model = Entities.objects.get(id=data['id'])

    if 'users_id' in data: 
        model = Entities.objects.get(users_id=data['users_id'])

    model.first_name = data['first_name']
    model.last_name = data['last_name']
    model.middle_name = data['middle_name']
    model.full_name = data['first_name'] +" "+ data['last_name']
    model.permanent_address = data['permanent_address']
    model.present_address = data['present_address']
    model.email = data['email']
    model.contact_number = data['contact_number']
    model.birthday = data['birthday']
    model.birth_place = data['birth_place']
    model.civil_status = data['civil_status']
    model.age = data['age']
    model.gender = data['gender']

    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    # like laravel query for faster process in frontend

    result = Entities.objects.values()

    return Response({'entity':result}, status=status.HTTP_200_OK)


def fetch(data, id):
    # model = Entities()

    result = Entities.objects.filter(id=id).values()

    return Response({'entity':result}, status=status.HTTP_200_OK)


def delete():
    #todo
    print()