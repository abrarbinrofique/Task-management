from django.shortcuts import render

from task.models import Task 
def home(request):
    form=Task.objects.all()
    print(form)
    return render (request,'base.html',{'form':form})