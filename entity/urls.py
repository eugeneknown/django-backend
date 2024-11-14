from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login', views.UsersTokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.RegisterView.as_view(), name='auth_register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    #region Entity
    path('entities/define', views.EntityDefine.as_view(), name='define'),
    path('entities/all', views.EntityAll.as_view(), name='all'),
    path('entities/fetch', views.EntityFetch.as_view(), name='fetch'),
    #endregion Entity

	#region Users
	path('users/define', views.UsersDefine.as_view(), name='define'),
    path('users/all', views.UsersAll.as_view(), name='all'),
    path('users/fetch', views.UsersFetch.as_view(), name='fetch'),
    #endregion Users

    #region Experience
	path('experience/define', views.ExperienceDefine.as_view(), name='define'),
    path('experience/all', views.ExperienceAll.as_view(), name='all'),
    path('experience/fetch', views.ExperienceFetch.as_view(), name='fetch'),
    path('experience/delete', views.ExperienceDelete.as_view(), name='delete'),
    path('experience/submit', views.ExperienceSubmit.as_view(), name='submit'),
    #endregion Experience

    #region ExperienceDetails
	path('experience/details/define', views.ExperienceDetailsDefine.as_view(), name='define'),
    path('experience/details/all', views.ExperienceDetailsAll.as_view(), name='all'),
    path('experience/details/fetch', views.ExperienceDetailsFetch.as_view(), name='fetch'),
    path('experience/details/delete', views.ExperienceDetailsDelete.as_view(), name='delete'),
    #endregion ExperienceDetails

    #region EntityDetails
	path('details/define', views.EntityDetailsDefine.as_view(), name='define'),
    path('details/all', views.EntityDetailsAll.as_view(), name='all'),
    path('details/fetch', views.EntityDetailsFetch.as_view(), name='fetch'),
    path('details/delete', views.EntityDetailsDelete.as_view(), name='delete'),
    #endregion EntityDetails

    #region EntityReference
	path('reference/define', views.EntityReferenceDefine.as_view(), name='define'),
    path('reference/all', views.EntityReferenceAll.as_view(), name='all'),
    path('reference/fetch', views.EntityReferenceFetch.as_view(), name='fetch'),
    path('reference/delete', views.EntityReferenceDelete.as_view(), name='delete'),
    path('reference/submit', views.EntityReferenceSubmit.as_view(), name='submit'),
    #endregion EntityReference

]