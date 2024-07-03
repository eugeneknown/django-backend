from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes

from hr.repository import CareersRepository
from hr.repository import EntityHasCareerRepository
from hr.repository import CareerQuestionsRepository
from hr.repository import CareerAnswersRepository
from hr.repository import CareerHasQuestionsRepository
from hr.repository import CareerTagsRepository

from entity.repository import EntityRepository

from files.repository import FilesRepository
from files.repository import EntityHasFilesRepository

# region Career

class CareersDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareersRepository.define(data=data)

        return result
    

class CareersAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareersRepository.all(data=data)

        return result
    

class CareersFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareersRepository.fetch(data=data, id=data['id'])
        
        return result
    

class CareersDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareersRepository.delete(id=data['id'])
        
        return result
    
#endregion Career    

#region EntityHasCareer
    
class EntityHasCareersDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasCareerRepository.define(data=data)

        return result
    

class EntityHasCareersAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasCareerRepository.all(data=data)

        return result
    

class EntityHasCareersFetch(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityHasCareerRepository.fetch(data=data, id=data['id'])
        
        return result
    

class EntityHasCareersReport(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = EntityHasCareerRepository.report(data=data)

        return result


class EntitySubmission(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        entity =  EntityHasCareerRepository.all(data={
            'filter': [
                {
                    'target': 'entity_id',
                    'operator': '=',
                    'value': data['entity']['id'] if 'entity_id' not in data else data['entity_id']
                }
            ]
        }).data
        if len(entity['entity_career']): return Response('Already Submitted', status=status.HTTP_400_BAD_REQUEST)

        if 'type' in data: 
            data['group'] = 'hr'
            upload = FilesRepository.filesUpload(data).data['files']
            files_id = FilesRepository.define(upload).data['files']['id']
            EntityHasFilesRepository.define({
                'entity_id': data['entity_id'],
                'files_id': files_id,
            })
            result = {'files_id': files_id}

        else:
            result = dict()
            result['answers'] = CareerAnswersRepository.define(data=data['answers']).data
            result['entity'] = EntityRepository.define(data['entity']).data
            result['career'] = EntityHasCareerRepository.define(data=data['career']).data
            
        return Response({'entity_career': result}, status=status.HTTP_200_OK)


#endregion EntityHasCareer

#region CareerTags
    
class CareerTagsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerTagsRepository.define(data=data)

        return result
    

class CareerTagsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerTagsRepository.all(data=data)

        return result
    

class CareerTagsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerTagsRepository.fetch(data=data, id=data['id'])
        
        return result
    

class CareerTagsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerTagsRepository.delete(id=data['id'])

        return result

#endregion CareerTags
    
#region CareerQuestions
    
class CareerQuestionsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerQuestionsRepository.define(data=data)

        return result
    

class CareerQuestionsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerQuestionsRepository.all(data=data)

        return result
    

class CareerQuestionsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerQuestionsRepository.fetch(data=data, id=data['id'])
        
        return result
    

class CareerQuestionsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerQuestionsRepository.delete(id=data['id'])
        
        return result

#endregion CareerQuestions
    
#region CareerHasQuestions
    
class CareerHasQuestionsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerHasQuestionsRepository.define(data=data)

        return result
    

class CareerHasQuestionsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerHasQuestionsRepository.all(data=data)

        return result
    

class CareerHasQuestionsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerHasQuestionsRepository.fetch(data=data, id=data['id'])
        
        return result
    

class CareerHasQuestionsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerHasQuestionsRepository.delete(id=data['id'])
        
        return result
    

class CareerHasQuestionsSort(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        result = CareerHasQuestionsRepository.sort(data=data)
        
        return result

#endregion CareerHasQuestions
    
#region CareerAnswers
    
class CareerAnswersDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerAnswersRepository.define(data=data)

        return result
    

class CareerAnswersAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerAnswersRepository.all(data=data)

        return result
    

class CareerAnswersFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerAnswersRepository.fetch(data=data, id=data['id'])
        
        return result

#endregion CareerAnswers