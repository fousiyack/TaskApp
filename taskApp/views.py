from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics,status
from .serializers import TaskSerializer
from userApp.models import CustomUser
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *

# Create your views here.

class taskList(viewsets.ModelViewSet):
    
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    def list(self, request, *args, **kwargs):
        taskList= Task.objects.all()
        serialized_data = self.get_serializer(taskList, many=True).data
        return render(request, 'tasks/taskList.html', {'tasks': serialized_data})

class AddTask(generics.CreateAPIView):
    serializer_class=TaskSerializer
    template_name='tasks/newTask.html'
    
    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)
    
    
    def create(self, request, *args, **kwargs):
        email = request.session.get('email')
     
        try:
            user = CustomUser.objects.get(email=email)
            
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist."})
        title = request.data.get('title')
        description = request.data.get('description')
        scheduled_at = request.data.get('scheduled_at')


        serializer = TaskSerializer(data={
        'user': user.id,
        'description': description,
        'title': title,
        'scheduled_at': scheduled_at,
    })
        if serializer.is_valid():
           serializer.save()
           print(serializer.data)
           return redirect('tasks')

        return Response(serializer.errors)
    


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        serializer = TaskSerializer(instance=task, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('tasks') 
    else:
        serializer = TaskSerializer(instance=task)

    return render(request, 'tasks/editTask.html', {'serializer': serializer, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
       
    
    

    
    
    
     
