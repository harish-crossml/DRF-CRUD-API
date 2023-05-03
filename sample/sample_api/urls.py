from django.conf import urls
from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', StudentView.as_view(), name='home'),
    path('student/<str:id>/', StudentView.as_view(), name='index'),
    #path('api/student/', StudentList.as_view(), name='students'),
    #path('api/students/<str:id>', StudentDetail.as_view(), name='students-detail'),

    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
