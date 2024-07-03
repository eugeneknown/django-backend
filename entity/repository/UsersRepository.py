from entity.models import Users, Entities

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Permission
from django.core import serializers as dserializers
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from datetime import datetime


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username')


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, users):
        token = super().get_token(users)

        token['user_id'] = users.id
        token['is_superusers'] = users.is_superuser
        token['is_staff'] = users.is_staff
        # token['permissions'] = permissionList(users.user_permissions.all())
        # token['group_permissions'] = groupList(users.groups.all())
        token['entity_id'] = users.entities.id
        token['full_name'] = users.entities.full_name
        token['first_name'] = users.entities.first_name
        token['last_name'] = users.entities.last_name
        token['middle_name'] = users.entities.middle_name
        token['permanent_address'] = users.entities.permanent_address
        token['present_address'] = users.entities.present_address
        token['image'] = users.entities.image
        token['email'] = users.entities.email
        token['email_verified'] = users.entities.email_verified
        token['email_verified_at'] = users.entities.email_verified_at
        token['contact_number'] = users.entities.contact_number
        # token['birthday'] = users.entities.birthday
        token['birth_place'] = users.entities.birth_place
        token['civil_status'] = users.entities.civil_status
        token['age'] = users.entities.age
        token['gender'] = users.entities.gender
        token['status'] = users.entities.status
        # token['created_at'] = users.entities.created_at
        # token['updated_at'] = users.entities.updated_at

        return token


def groupList(model):
    result = dict()
    range = 0
    for item in model:
        result[range] = model_to_dict(item)
        result[range]['permissions'] = permissionList(item.permissions.all())
        range+=1

    return result


def permissionList(model):
    result = dict()
    range = 0
    for item in model:
        result[range] = model_to_dict(item)
        range+=1

    return result


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
    # number = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        # fields =  ('username', 'password', 'confirm_password', 'id')
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"Authentication": "Password didn't match."})
        
        return attrs

    def create(self, data):
        
        users = Users.objects.create(username=data['username'])

        users.set_password(data['password'])
        users.save()

        entity = Entities()
        entity.users = users
        # entity.first_name = data['first_name']
        # entity.last_name = data['last_name']
        # entity.full_name = (data['first_name'] +' '+data['last_name']).title()
        # entity.email = data['email']
        # entity.contact_number = data['number']
        entity.save()

        return users
    

def define(data):
    model = Users()

    if 'id' in data:
        model = Users.objects.get(id=data['id'])

    model.email = data['email']
    model.username = data['username']
    model.password = data['password']

    now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")
    model.created_at = now
    model.updated_at = now

    model.save()

    return Response(status=status.HTTP_200_OK)


def all(data):
    # like laravel query for faster process in frontend

    result = Users.objects.values()

    return Response({'users': result}, status=status.HTTP_200_OK)


def fetch(data, id):

    result = Users.objects.filter(id=id).values()

    return Response({'users':result}, status=status.HTTP_200_OK)


def delete():
    #todo
    print()