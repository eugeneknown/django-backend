from hr.models import Careers

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'careers'
now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")

def define(data):
    model = Careers()

    if 'id' in data:
        model = Careers.objects.get(id=data['id'])

    model.title = data['title']
    model.type = data['type']
    model.salary = data['salary']
    model.benifits = data['benifits']
    model.pay_types = '0' #data['pay_types']
    model.experience = data['experience']
    model.descriptions = data['descriptions']
    model.qualifications = '0' #data['qualifications']
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response(status=status.HTTP_200_OK)


def all(data):
    result = dict()

    if 'relations' in data:
        object = Careers.objects.filter().exclude(deleted_at__isnull=False).all()
        range = 0
        for item in object:
            # value = dict()
            value =  model_to_dict(item)
            if 'has' in data['relations']:
                has = item.hasquestions.exclude(deleted_at__isnull=False).all()
                _range = 0
                _result = dict()
                for _item in has:
                    _result[_range] = model_to_dict(_item)
                    if 'questions' in data['relations']:
                        _result[_range]['questions'] = model_to_dict(_item.questions)

                    _range+=1
                    
                value['has'] = _result
                result[range] = value
                range+=1

    else:
        result = Careers.objects.values()
    

    # print(result)
    return Response({meta_data: result}, status=status.HTTP_200_OK)


# all({'relations' : ['questions', 'has']})


def fetch(data, id):
    result = Careers.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    model = Careers.objects.get(id=id)

    model.deleted_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)