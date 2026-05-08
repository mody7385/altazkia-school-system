from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ArabicLoginView(LoginView):
    template_name = 'accounts/login.html'

class ArabicLogoutView(LogoutView):
    pass

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
