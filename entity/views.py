from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Users
from entity.repository import EntityRepository
from entity.repository import UsersRepository
from entity.repository import ExperienceRepository
from entity.repository import EntityHasExperienceRepository
from entity.repository import EntityDetailsRepository

# from .repository.EntitiesRepository import EntitiesRepository

#region Entity


class UsersTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsersRepository.UserTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UsersRepository.RegisterSerializer


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        refresh = request.data['refresh']
        token = RefreshToken(refresh)
        token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)


class EntityDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityRepository.define(data=data)

        return result
    

class EntityAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        result = EntityRepository.all(data=data)

        return result
    

class EntityFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityRepository.fetch(data=data, id=data['id'])

        return result
    
#endregion Entity
    
#region Users

class UsersDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = UsersRepository.define(data=data)

        return result
    

class UsersAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        result = UsersRepository.all(data=data)

        return result
    

class UsersFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = UsersRepository.fetch(data=data, id=data['id'])

        return result

#endregion Users

#region Experience

class ExperienceDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = ExperienceRepository.define(data=data)

        return result
    

class ExperienceAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        result = ExperienceRepository.all(data=data)

        return result
    

class ExperienceFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = ExperienceRepository.fetch(data=data, id=data['id'])

        return result
    

class ExperienceDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = ExperienceRepository.delete(id=data['id'])

        return result

#endregion Experience

#region EntityHasExperience

class EntityHasExperienceDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasExperienceRepository.define(data=data)

        return result
    

class EntityHasExperienceAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        result = EntityHasExperienceRepository.all(data=data)

        return result
    

class EntityHasExperienceFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityHasExperienceRepository.fetch(data=data, id=data['id'])

        return result
    

class EntityHasExperienceDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityHasExperienceRepository.delete(id=data['id'])

        return result

#endregion EntityHasExperience

#region EntityDetails

class EntityDetailsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityDetailsRepository.define(data=data)

        return result
    

class EntityDetailsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        data = request.data
        result = EntityDetailsRepository.all(data=data)

        return result
    

class EntityDetailsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityDetailsRepository.fetch(data=data, id=data['id'])

        return result
    

class EntityDetailsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityDetailsRepository.delete(id=data['id'])

        return result

#endregion EntityDetails