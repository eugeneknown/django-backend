from django.shortcuts import render
from django.forms.models import model_to_dict

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
from entity.repository import ExperienceDetailsRepository
from entity.repository import EntityDetailsRepository
from entity.repository import EntityReferenceRepository

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
    def post(self, request):
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
    def post(self, request):
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
    def post(self, request):
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
    

class ExperienceSubmit(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        # additional validations last company, total and other experience

        # todo - The user has permission to freely 
        # edit their company experience as well as their
        # character references. In this regard, the user 
        # already has access to data that they can manipulate as needed.
        # If the user already has existing data, they can use or 
        # edit it when applying for another position.

        # revision of company experience, the schema can be found at draw.io

        # details  = ExperienceDetailsRepository.all(data={
        #     'filter': [{
        #         'operator': '=',
        #         'target': 'entity_id',
        #         'value': data['entity_id'],
        #     }]
        # }).data['has_experience']

        # if details:
        #     for item in details:
        #         ExperienceDetailsRepository.delete(id=item['id'])


        exp = ExperienceRepository.fetch(data={}, id=data['entity_id']).data['experience']
        
        if not exp:
            exp = ExperienceRepository.define(data={
                'entity_id': data['entity_id'],
                'total_experience': data['experience']['total_experience'],
                'other_experience': data['experience']['other_experience'],
            }).data['experience']
        else: 
            exp = exp[0]

        for item in data['experience']:
            if data['experience'][item] and type(data['experience'][item]) is dict:
                details = ExperienceDetailsRepository.all(data={
                    'filter': [
                        {
                            'operator': '=',
                            'target': 'experience_id',
                            'value': exp['id'],
                        },
                        {
                            'operator': '=',
                            'target': 'order',
                            'value': item,
                        },
                    ]
                }).data['experience_details']

                detailsData = dict(data['experience'][item])
                detailsData['order'] = item
                if details:
                    detailsData['id'] = details[0]['id']
                else:
                    detailsData['experience_id'] = exp['id']

                
                ExperienceDetailsRepository.define(data=detailsData)


        result = ExperienceDetailsRepository.all(data={
            'filter': [{
                'operator': '=',
                'target': 'experience_id',
                'value': exp['id'],
            }]
        }).data['experience_details']

        return Response({'experience': result}, status=status.HTTP_200_OK)


#endregion Experience

#region ExperienceDetails

class ExperienceDetailsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = ExperienceDetailsRepository.define(data=data)

        return result
    

class ExperienceDetailsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = ExperienceDetailsRepository.all(data=data)

        return result
    

class ExperienceDetailsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = ExperienceDetailsRepository.fetch(data=data, id=data['id'])

        return result
    

class ExperienceDetailsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = ExperienceDetailsRepository.delete(id=data['id'])

        return result


#endregion ExperienceDetails

#region EntityDetails

class EntityDetailsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityDetailsRepository.define(data=data)

        return result
    

class EntityDetailsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
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

#region EntityReference

class EntityReferenceDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityReferenceRepository.define(data=data)

        return result
    

class EntityReferenceAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityReferenceRepository.all(data=data)

        return result
    

class EntityReferenceFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityReferenceRepository.fetch(data=data, id=data['id'])

        return result
    

class EntityReferenceDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityReferenceRepository.delete(id=data['id'])

        return result
    

class EntityReferenceSubmit(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        result = dict()
        ref = EntityReferenceRepository.fetch(data={}, id=data['entity_id']).data['entity_reference']
        count = 0
        for item in data['reference']:
            if data['reference'][item] and type(data['reference'][item]) is dict:
                temp = data['reference'][item]
                temp['entity_id'] = data['entity_id']
                if not ref:
                    if 0 in ref:
                        temp['id'] = ref['id']

            result[count] = EntityReferenceRepository.define(data=temp).data['entity_reference']
            count+=1

        return Response({'reference': result}, status=status.HTTP_200_OK)

#endregion EntityReference