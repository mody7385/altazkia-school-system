from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

MODEL = list(globals().values())[-1]
class GenericList(LoginRequiredMixin,ListView): model=MODEL; template_name='circles/list.html'
class GenericCreate(LoginRequiredMixin,CreateView): model=MODEL; fields='__all__'; template_name='shared/form.html'; success_url=reverse_lazy('circles:list')
class GenericUpdate(GenericCreate,UpdateView): pass
class GenericDelete(LoginRequiredMixin,DeleteView): model=MODEL; template_name='shared/confirm_delete.html'; success_url=reverse_lazy('circles:list')
