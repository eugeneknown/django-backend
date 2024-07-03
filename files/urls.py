from django.urls import path
from . import views


urlpatterns = [
    
    #region Files

    path('files/upload', views.FilesUpload.as_view(), name='upload'),
    path('files/define', views.FilesDefine.as_view(), name='define'),
    path('files/all', views.FilesAll.as_view(), name='all'),
    path('files/fetch', views.FilesFetch.as_view(), name='fetch'),
    path('files/delete', views.FilesDelete.as_view(), name='delete'),

    #endregion Files

    #region EntityHasFiles

    path('files/entity/define', views.EntityHasFilesDefine.as_view(), name='define'),
    path('files/entity/all', views.EntityHasFilesAll.as_view(), name='all'),
    path('files/entity/fetch', views.EntityHasFilesFetch.as_view(), name='fetch'),
    path('files/entity/delete', views.EntityHasFilesDelete.as_view(), name='delete'),

    #endregion EntityHasFiles

]