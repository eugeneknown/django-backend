from django.shortcuts import render

from backend.globalFunctions import *

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
from hr.repository import CareerPlatformsRepository
from hr.repository import ScheduleRepository
from hr.repository import ScheduleDetailsRepository
from hr.repository import TimeSheetRepository
from hr.repository import TimeSheetDetailsRepository
from hr.repository import TimeLogsRepository

from entity.repository import EntityRepository

from files.repository import FilesRepository
from files.repository import EntityHasFilesRepository

from django.utils import timezone

from datetime import datetime

from random import randint

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
    

class EntityHasCareersDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = EntityHasCareerRepository.delete(id=data['id'])

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
                },
                {
                    'target': 'careers_id',
                    'operator': '=',
                    'value': data['career']['careers_id'] if 'careers_id' not in data else data['careers_id']
                },
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


class EntityAddRandomBullshit(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        result = dict()

        career_range = 16
        entity_range = 24
        platforms_range = 3

        add = 10

        range = ['2024-08-04 00:00:00', '2024-08-10 23:59:59']

        #todo add created_at random range
        for i in range(add):
            result[i] = EntityHasCareerRepository.define(data={
                'careers_id': randint(0, career_range),
                'entity_id': randint(0, entity_range),
                'platforms_id': randint(0, platforms_range),
            }).data


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

#region CareerPlatforms
    
class CareerPlatformsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerPlatformsRepository.define(data=data)

        return result
    

class CareerPlatformsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = CareerPlatformsRepository.all(data=data)

        return result
    

class CareerPlatformsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerPlatformsRepository.fetch(data=data, id=data['id'])
        
        return result
    

class CareerPlatformsDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = CareerPlatformsRepository.delete(id=data['id'])

        return result

#endregion CareerPlatforms
    
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
    

class CareerHasQuestionsMove(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        result = CareerHasQuestionsRepository.move(data=data)
        
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

#region TimeLogs
    
class TimeLogsDefine(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = dict()
        if not 'action' in data:
            return Response('Timelogs action not found', status=status.HTTP_404_NOT_FOUND)


        schedule = ScheduleRepository.all(data={
            'filter': [
                {
                    'target': 'entity_id',
                    'operator': '=',
                    'value': data['entity_id'],
                }
            ],
            'relations': ['schedule_details'],
        })

        if status_error(schedule):
            return Response('Schedule not found', status=status.HTTP_404_NOT_FOUND)
        
        schedule = schedule.data['schedule'][0]
        
        if not schedule['schedule_details_data']:
            return Response('Schedule Details not found', status=status.HTTP_404_NOT_FOUND)

        details = schedule['schedule_details_data']
        time_start = dict()
        time_end = dict()
        
        format = '%H:%M:%S'
        range = 0
        for item in details:
            time_start[range] = details[item]['time_start'] #formatDateTime(details[item]['time_start'], format)
            time_end[range] = details[item]['time_end'] #formatDateTime(details[item]['time_end'], format)
            range+=1

        # currenDate = dateTimeNow().replace()

        # return Response([details, time_start, time_end])

        timelogs = TimeLogsRepository.lastLogCheck(
            data['entity_id']
        )
        now = datetime.now()

        if not status_error(timelogs):
            timelogs = timelogs.data['time_logs']

            duration = now - timelogs['log_start'].replace(tzinfo=None)

            # over write the previous log
            result.update(TimeLogsRepository.define({
                'id': timelogs['id'],
                'duration': duration.total_seconds(),
                'log_end': datetime.now(),
            }).data)

        if not 'end' in data['action']:
            result.update(TimeLogsRepository.define({
                'entity_id': data['entity_id'],
                'log_start': now,
            }).data)

        return Response({'time_logs': result}, status=status.HTTP_200_OK)
    

class TimeLogsAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        result = TimeLogsRepository.all(data=data)

        return result
    

class TimeLogsFetch(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        if 'id' not in data:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        result = TimeLogsRepository.fetch(data=data, id=data['id'])
        
        return result

#endregion TimeLogs