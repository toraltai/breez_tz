from django.urls import path, include
from .views import *


urlpatterns = [
    path('api/v1/file', FileAPI.as_view()),
    path('api/v1/info', UserItemAPI.as_view()),

]
