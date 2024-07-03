from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from entity.repository import EntityRepository
from .models import Users
from entity.repository import UsersRepository

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
    def get(self, request):
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