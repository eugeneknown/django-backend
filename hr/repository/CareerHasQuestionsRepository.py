from hr.models import CareerHasQuestions, Careers, CareerQuestions

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status

from datetime import datetime


meta_data = 'career_questions'
now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")


def define(data):
    model = CareerHasQuestions()

    if 'id' in data:
        model = CareerHasQuestions.objects.get(id=data['data'])
    else:
        model.careers = Careers.objects.get(id=data['careers_id'])
        model.questions = CareerQuestions.objects.get(id=data['questions_id'])

    model.order = data['order']
    model.section = data['section']
    
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    object = CareerHasQuestions.objects.exclude(deleted_at__isnull=False).order_by('order').all()
    if 'careers_id' in data:
        object = CareerHasQuestions.objects.filter(careers=data['careers_id']).exclude(deleted_at__isnull=False).order_by('order')
    elif 'questions_id' in data:
        object = CareerHasQuestions.objects.filter(questions=data['questions_id']).exclude(deleted_at__isnull=False).order_by('order')

    if 'relations' in data:
        range = 0
        for item in object:
            value =  model_to_dict(item)
            if 'questions' in data['relations']:
                value['questions'] = model_to_dict(item.questions)
                result[range] = value
                range+=1

            if 'careers' in data['relations']:
                value['careers'] = model_to_dict(item.careers)
                result[range] = value
                range+=1

    else:
        result = CareerHasQuestions.objects.values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = CareerHasQuestions.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = CareerHasQuestions.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def sort(data):
    result = dict()

    for item in data:
        result[item] = {}

        for _item in data[item]:
            model = CareerHasQuestions.objects.get(id=data[item][_item]['has_id'])
            model.order = int(_item)
            model.save()

            temp = model_to_dict(model)
            temp['questions'] = model_to_dict(model.questions)
            
            result[item][_item] = temp


    return Response({meta_data: result}, status=status.HTTP_200_OK)
