from django.urls import path
from .views import GenericList, GenericCreate, GenericUpdate, GenericDelete
app_name='reports'
urlpatterns=[path('',GenericList.as_view(),name='list'),path('add/',GenericCreate.as_view(),name='add'),path('<int:pk>/edit/',GenericUpdate.as_view(),name='edit'),path('<int:pk>/delete/',GenericDelete.as_view(),name='delete')]
