from backend.globalFunctions import *
from hr.models import CareerAnswers, CareerHasQuestions, CareerQuestions, Careers
from entity.models import Entities
from files.models import Files

from files.repository import FilesRepository, EntityHasFilesRepository

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'career_answers'


def define(data):
    result = dict()
    count = 0

    for key in data:
        model = CareerAnswers()
        item = data[key]

        if 'id' in item:
            model = model.objects.get(id=data['id'])

        if 'type' in item:
            model.files = Files.objects.get(id=int(item['files_id']))

        else:
            model.files = None


        model.entity = Entities.objects.get(id=int(item['entity_id']))
        model.careers = Careers.objects.get(id=int(item['careers_id']))
        model.question = CareerQuestions.objects.get(id=int(item['question_id']))
        model.value = item['value']
        
        now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
        model.created_at = now
        model.updated_at = now

        model.save()

        result[count] = model_to_dict(model)
        count+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = CareerAnswers.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['question_data'] = model_to_dict(item.question)
        value['entity_data'] = model_to_dict(item.entity)
        if item.files is not None: 
            value['files'] = FilesRepository.fetch(item.files_id).data['files'][0]
            value['files_url'] = FilesRepository.filesUrl(item.files_id).data['files']
        result[range] = value
        range+=1

    return Response({meta_data: result}, status=status.HTTP_200_OK)


# all({'entity_id': 1, 'careers_id': 1})

def fetch(data, id):
    result = CareerAnswers.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()