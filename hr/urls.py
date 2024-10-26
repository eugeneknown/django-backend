from django.urls import path
from . import views


urlpatterns = [
    
    #region Careers
    path('careers/define', views.CareersDefine.as_view(), name='define'),
    path('careers/all', views.CareersAll.as_view(), name='all'),
    path('careers/fetch', views.CareersFetch.as_view(), name='fetch'),
    path('careers/delete', views.CareersDelete.as_view(), name='delete'),
    #endregion Careers

    #region EntityHasCareer

    path('careers/entity/define', views.EntityHasCareersDefine.as_view(), name='define'),
    path('careers/entity/all', views.EntityHasCareersAll.as_view(), name='all'),
    path('careers/entity/fetch', views.EntityHasCareersFetch.as_view(), name='fetch'),
    path('careers/entity/delete', views.EntityHasCareersDelete.as_view(), name='delete'),
    path('careers/entity/report', views.EntityHasCareersReport.as_view(), name='report'),
    path('careers/entity/submit', views.EntitySubmission.as_view(), name='submit'),

    #endregion EntityHasCareer

    #region CareerTags

    path('careers/tags/define', views.CareerTagsDefine.as_view(), name='define'),
    path('careers/tags/all', views.CareerTagsAll.as_view(), name='all'),
    path('careers/tags/fetch', views.CareerTagsFetch.as_view(), name='fetch'),
    path('careers/tags/delete', views.CareerTagsDelete.as_view(), name='delete'),

    #endregion CareerTags

    #region CareerPlatforms

    path('careers/platform/define', views.CareerPlatformsDefine.as_view(), name='define'),
    path('careers/platform/all', views.CareerPlatformsAll.as_view(), name='all'),
    path('careers/platform/fetch', views.CareerPlatformsFetch.as_view(), name='fetch'),
    path('careers/platform/delete', views.CareerPlatformsDelete.as_view(), name='delete'),

    #endregion CareerPlatforms

    #region CareerQuestions

    path('careers/questions/define', views.CareerQuestionsDefine.as_view(), name='define'),
    path('careers/questions/all', views.CareerQuestionsAll.as_view(), name='all'),
    path('careers/questions/fetch', views.CareerQuestionsFetch.as_view(), name='fetch'),
    path('careers/questions/delete', views.CareerQuestionsDelete.as_view(), name='delete'),

    #endregion CareerQuestions

    #region CareerHasQuestions

    path('careers/has/questions/define', views.CareerHasQuestionsDefine.as_view(), name='define'),
    path('careers/has/questions/all', views.CareerHasQuestionsAll.as_view(), name='all'),
    path('careers/has/questions/fetch', views.CareerHasQuestionsFetch.as_view(), name='fetch'),
    path('careers/has/questions/delete', views.CareerHasQuestionsDelete.as_view(), name='delete'),
    path('careers/has/questions/sort', views.CareerHasQuestionsSort.as_view(), name='sort'),
    path('careers/has/questions/move', views.CareerHasQuestionsMove.as_view(), name='move'),

    #endregion CareerHasQuestions

    #region CareerAnswers

    path('careers/answers/define', views.CareerAnswersDefine.as_view(), name='define'),
    path('careers/answers/all', views.CareerAnswersAll.as_view(), name='all'),
    path('careers/answers/fetch', views.CareerAnswersFetch.as_view(), name='fetch'),

    #endregion CareerAnswers

    #region TimeLogs

    path('timesheet/logs/define', views.TimeLogsDefine.as_view(), name='define'),
    path('timesheet/logs/all', views.TimeLogsAll.as_view(), name='all'),
    path('timesheet/logs/fetch', views.TimeLogsFetch.as_view(), name='fetch'),

    #endregion TimeLogs

]