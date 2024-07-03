from hr.models import CareerQuestions

from rest_framework.response import Response
from rest_framework import status

from django.forms.models import model_to_dict

from datetime import datetime


meta_data = 'career_questions'
now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")


def define(data):
    model = CareerQuestions()

    if 'id' in data:
        model = CareerQuestions.objects.get(id=data['id'])

    model.title = data['title']
    model.value = data['value'] if 'value' in data else ''
    model.type = data['type']
    
    now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = CareerQuestions.objects.exclude(deleted_at__isnull=False).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = CareerQuestions.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = CareerQuestions.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)