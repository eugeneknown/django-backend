from backend.globalFunctions import *
from hr.models import CareerAnswers, CareerQuestions, Careers, EntityHasCareer
from entity.models import Entities
from files.models import Files

from files.repository import FilesRepository

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'career_answers'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")


def define(data):
    model = CareerAnswers()

    if 'id' in data:
        model = CareerAnswers.objects.get(id=data['id'])
        
    else:
        if 'files_id' in data: model.files = Files.objects.get(id=data['files_id'])

    model.entity = Entities.objects.get(id=int(data['entity_id']))
    model.careers = Careers.objects.get(id=int(data['careers_id']))
    model.question = CareerQuestions.objects.get(id=int(data['question_id']))
    model.entitycareer = EntityHasCareer.objects.get(id=int(data['entity_career_id']))
    model.value = data['value']
    
    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    object = CareerAnswers.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    range = 0
    for item in object:
        value =  model_to_dict(item)
        if 'relations' in data:
            if 'question' in data['relations']:
                value['question_data'] = model_to_dict(item.question)

            if 'entity' in data['relations']:
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