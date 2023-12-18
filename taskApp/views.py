from django.shortcuts import render

# Create your views here.

def taskList(request):
    return render(request,'tasks/taskList.html')
