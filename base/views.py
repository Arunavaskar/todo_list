from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    #form_class = form_model_name
    #we can create a model for the form and then assign
    #that model form to form_class attribute instead 
    #of using fields
    success_url = reverse_lazy('tasks')