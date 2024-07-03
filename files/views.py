from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser

from files.repository import FilesRepository, EntityHasFilesRepository

from entity.repository import EntityRepository

# region Files

class FilesUpload(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        data = request.data
        result = FilesRepository.filesUpload(data=data)

        return result


class FilesDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = FilesRepository.define(data=data)

        return result
    

class FilesAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = FilesRepository.all(data=data)

        return result
    

class FilesFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = FilesRepository.fetch(data=data, id=data['id'])
        
        return result
    

class FilesDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = FilesRepository.delete(id=data['id'])
        
        return result
    
#endregion Files    

#region EntityHasFiles
    
class EntityHasFilesDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasFilesRepository.define(data=data)

        return result
    

class EntityHasFilesAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasFilesRepository.all(data=data)

        return result
    

class EntityHasFilesFetch(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityHasFilesRepository.fetch(data=data, id=data['id'])
        
        return result
    

class EntityHasFilesDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasFilesRepository.delete(data=data)

        return result


#endregion EntityHasFiles