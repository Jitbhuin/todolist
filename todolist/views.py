from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
  print(request)
  todo_list=models.ToDo.objects.all().order_by('-added_time')

  return render(request, 'todolist/add_todo.html',{'todo_list':todo_list})

@csrf_exempt
def add_todo(request):
  added_item = request.POST.get('added_item')
  print(added_item)
  obj= models.ToDo.objects.create(added_time=timezone.now(), todo=added_item)
  print(obj)
  return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request,todo_id):
  print(todo_id)
  models.ToDo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')
