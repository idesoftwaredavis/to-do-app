from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from .models import Task
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
class home(View):
    def get(self, request, *args, **kwargs):
        registros = Task.objects.all()
        if request.method=='GET' and request.is_ajax():
            print()
            id=request.GET.get('id')
            tarea = Task.objects.get(task_id=id)
            print()
            print(tarea)
            data ={}
            data['descripcion']=tarea.task_description
            return JsonResponse({'data':data}, status=200)
        return render(request, 'todo.html', {'model':registros})

    def post(self, request, *args, **kwargs):
        modelObject = Task()
        task = request.POST.get('tarea')
        description = request.POST.get('descripcion')
        date = request.POST.get('fecha')
        data={
            'task':task,
            'description':description,
            'date':date
        }
        modelObject.task_name=task
        modelObject.task_description=description
        modelObject.date= datetime.strptime(date, '%Y-%m-%d')
        modelObject.save()
        #serialized_obj = serializers.serialize('json', [ registros, ])
        return JsonResponse({'data':data}, status=200)
