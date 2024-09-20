from backend.globalFunctions import *
from hr.models import EntityHasCareer, Careers, CareerTags, CareerPlatforms
from entity.models import Entities

from django.forms.models import model_to_dict
from django.db.models import Q, Count, Case, Value, When, IntegerField, F
from django.db.models.functions import Trunc, Coalesce

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


meta_data = 'entity_career'


def define(data):
    model = EntityHasCareer()

    if 'id' in data:
        model = EntityHasCareer.objects.get(id=data['id'])

    if 'careers_id' in data: model.careers = Careers.objects.get(id=int(data['careers_id']))
    if 'entity_id' in data: model.entity = Entities.objects.get(id=int(data['entity_id']))
    if 'platforms_id' in data: model.platforms = CareerPlatforms.objects.get(id=int(data['platforms_id']))
    if 'tags_id' in data:
        if data['tags_id'] == None:
            model.tags = None
        else:
            model.tags = CareerTags.objects.get(id=int(data['tags_id']))
    
    now = timezone.now() #.strftime("%d-%m-%Y %H:%M:%S")
    if model.created_at is None: model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    result = dict()

    filter = genericModelFilter(data)
    # print(filter)
    object = EntityHasCareer.objects.filter(**filter['filter']).exclude(Q(**filter['exclude'], _connector=Q.OR))
    if 'order' in data: object = object.order_by('-'+data['order']['target'] if data['order']['value'] == 'desc' else data['order']['target'])
    # print(object.query)
    range = 0
    for item in object:
        value =  model_to_dict(item)
        value['careers_data'] = model_to_dict(item.careers)
        value['entity_data'] = model_to_dict(item.entity)
        value['platforms_data'] = model_to_dict(item.platforms)
        if item.tags is not None: value['tags_data'] = model_to_dict(item.tags)
        result[range] = value
        range+=1

    # print(result)
    return Response({meta_data: result}, status=status.HTTP_200_OK)

# all({
#     'filter': [
#         {
#             'target': 'created_at',
#             'operator': 'range',
#             'value': ['2024-03-05', '2024-03-08 23:59:59'],
#         },
#     ],
# })

def fetch(data, id):
    result = EntityHasCareer.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()


def report(data):
    result = dict()
    filter = genericModelFilter(data)

    if 'date' in data: 
        object = EntityHasCareer.objects.filter(
            **filter['filter']
        ).exclude(
            Q(**filter['exclude'], _connector=Q.OR)
        ).values(
            date=Trunc(data['date']['target'], data['date']['operator']),
        ).annotate(
            count=Count(data['date']['value'])
        ).order_by('date')

        result = object
    
    if 'tags' in data:
        object = EntityHasCareer.objects.filter(
            **filter['filter']
        ).exclude(
            Q(**filter['exclude'], _connector=Q.OR)
        ).values(
            # date=Trunc('created_at', 'month'),
            tag_id=Coalesce('tags', 0),
        ).annotate(
            count=Count('tag_id')
        ).order_by('tag_id')

        result = object

    if 'platforms' in data:
        object = EntityHasCareer.objects.filter(
            **filter['filter']
        ).exclude(
            Q(**filter['exclude'], _connector=Q.OR)
        ).values(
            platform_id=Coalesce('platforms', 0),
            date=Trunc(data['platforms']['target'], data['platforms']['operator']),
        ).annotate(
            count=Count(data['platforms']['value'])
        ).order_by('date')

        range = 0
        for item in object:
            value = item
            value['platform_data'] = CareerPlatforms.objects.filter(id=item['platform_id']).values()[0]
            result[range] = value
            range+=1

        # print(result)
    
    return Response({meta_data: result}, status=status.HTTP_200_OK)

# report({
#     'filter': [
#         {
#             'target': 'created_at',
#             'operator': 'range',
#             'value': ['2024-08-03', '2024-08-10 23:59:59'],
#         },
#     ],
#     'platforms': {
#         'operator': 'day',
#         'target': 'created_at',
#         'value': 'id',
#     },
# })