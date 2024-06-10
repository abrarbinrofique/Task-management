from django.shortcuts import render,redirect

from task.forms import new_task

from task.models import Task
# Create your views here.

def add_task(request):
    if request.method=='POST':
        tasks=new_task(request.POST)
        tasks.is_valid()
        tasks.save()
        # print(tasks.cleaned_data)

    else:

        tasks=new_task()
    
    return render(request,'task.html',{'form':tasks})





def edit_task(request,id):
    newtask=Task.objects.get(pk=id)
    task_form=new_task(instance=newtask)
    if request.method=='POST':
        tasks=new_task(request.POST,instance=newtask)
        tasks.is_valid()
        tasks.save()
        return redirect ('home')
    
    return render(request,'task.html',{'form':task_form})


def delete_task(request,id):
    Task.objects.get(pk=id).delete()
    
    return redirect ('home')