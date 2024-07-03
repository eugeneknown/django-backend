from backend.globalFunctions import *

from files.models import Files

from rest_framework.response import Response
from rest_framework import status

from django.forms.models import model_to_dict
from django.db.models import Q

from datetime import datetime
from hashlib import md5
from time import time

from storages.backends.gcloud import GoogleCloudStorage


meta_data = 'files'

def filesUpload(data):
    result = dict()
    storage = GoogleCloudStorage()
    hash = md5(str(round(time() * 1000)).encode()).hexdigest()

    # validation
    if 'file' not in data: Response({meta_data: 'missing file in data parameters'}, status=status.HTTP_417_EXPECTATION_FAILED)
    if 'entity_id' not in data: Response({meta_data: 'missing entity ID in data parameters'}, status=status.HTTP_417_EXPECTATION_FAILED)
    if 'group' not in data: Response({meta_data: 'missing group in data parameters'}, status=status.HTTP_417_EXPECTATION_FAILED)

    filename = data['file'].name
    path = data['group'] +'/'+ data['entity_id'] +'/'+ hash +'/'+ filename
    if not storage.save(path, data['file']):
        return Response({meta_data: 'File failed to upload'}, status=status.HTTP_400_BAD_REQUEST)
    # url = storage.url(path)
    result['hash'] = hash
    result['group_permission'] = data['group']
    result['file_path'] = path
    result['file_size'] = data['file'].size
    result['file_type'] = data['type'] if data['type'] else ''

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def filesUrl(id):
    storage = GoogleCloudStorage()

    url = Files.objects.filter(id=id).values('file_path')[0]
    return Response({meta_data: storage.url(url['file_path'])}, status=status.HTTP_200_OK)


def define(data):
    model = Files()

    if 'id' in data:
        model = Files.objects.get(id=data['id'])

    model.hash = data['hash']
    model.group_permission = data['group_permission']
    model.file_path = data['file_path']
    model.file_type = data['file_type']
    model.file_size = data['file_size']

    now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response({meta_data: model_to_dict(model)}, status=status.HTTP_200_OK)


def all(data):
    filter = genericModelFilter(data)
    result = Files.objects.filter(**filter['filter'][0]).exclude(Q(**filter['exclude'][0], _connector=Q.OR)).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def fetch(data, id):
    result = Files.objects.filter(id=id).values()

    return Response({meta_data: result}, status=status.HTTP_200_OK)


def delete(id):
    print()