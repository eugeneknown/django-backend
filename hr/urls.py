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
    path('careers/entity/report', views.EntityHasCareersReport.as_view(), name='report'),
    path('careers/entity/submit', views.EntitySubmission.as_view(), name='submit'),

    #endregion EntityHasCareer

    #region CareerTags

    path('careers/tags/define', views.CareerTagsDefine.as_view(), name='define'),
    path('careers/tags/all', views.CareerTagsAll.as_view(), name='all'),
    path('careers/tags/fetch', views.CareerTagsFetch.as_view(), name='fetch'),
    path('careers/tags/delete', views.CareerTagsDelete.as_view(), name='delete'),

    #endregion CareerTags

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

    #endregion CareerHasQuestions

    #region CareerAnswers

    path('careers/answers/define', views.CareerAnswersDefine.as_view(), name='define'),
    path('careers/answers/all', views.CareerAnswersAll.as_view(), name='all'),
    path('careers/answers/fetch', views.CareerAnswersFetch.as_view(), name='fetch'),

    #endregion CareerAnswers

]