from django.urls import path
from .views import DashboardHome
app_name='dashboard'
urlpatterns=[path('',DashboardHome.as_view(),name='home')]
