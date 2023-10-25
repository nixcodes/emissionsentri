from django.urls import path
from .views import emissionsListCreate

urlpatterns = [
    path('emissions/', emissionsListCreate.as_view(), name='emissions-list-create'),
]