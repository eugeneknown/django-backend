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

]