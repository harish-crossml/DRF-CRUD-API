from django.conf import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentView.as_view(), name='home'),
    path('api/<str:id>/', StudentView.as_view(), name='index'),
    #path('api/student/', StudentList.as_view(), name='students'),
    #path('api/students/<str:id>', StudentDetail.as_view(), name='students-detail'),
]
