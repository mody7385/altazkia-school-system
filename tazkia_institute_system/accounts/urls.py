from django.urls import path
from .views import ArabicLoginView, ArabicLogoutView, ProfileView
app_name='accounts'
urlpatterns=[path('login/',ArabicLoginView.as_view(),name='login'),path('logout/',ArabicLogoutView.as_view(),name='logout'),path('profile/',ProfileView.as_view(),name='profile')]
