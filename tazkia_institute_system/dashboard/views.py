from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from students.models import Student
from circles.models import Circle
from accounts.models import Teacher,Supervisor,Parent

class DashboardHome(LoginRequiredMixin,TemplateView):
    template_name='dashboard/home.html'
    def get_context_data(self,**kwargs):
        c=super().get_context_data(**kwargs)
        c.update({'students_count':Student.objects.count(),'circles_count':Circle.objects.count(),'teachers_count':Teacher.objects.count(),'supervisors_count':Supervisor.objects.count(),'parents_count':Parent.objects.count()})
        return c
