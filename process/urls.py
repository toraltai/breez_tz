from django.urls import path, include
from .views import *


urlpatterns = [
    path('v1/add-deals', add_deals),
    path('v1/top5', UserItemAPI.as_view()),
]
