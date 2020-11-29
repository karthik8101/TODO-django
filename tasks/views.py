from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .forms import *
def index(request):
    tasks=Task.objects.order_by('-created')
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
    
        if form.is_valid():
            form.save()
        else:
            print('form is not complete')
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)
def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update_task.html',context)

def deletetask(request,pk):
    item=Task.objects.get(id=pk)
    context={'item':item}
    if request.method=='POST':
        item.delete()
        messages.info(request,"item removed  !!!")
        return redirect('/')

    return render(request,'delete.html',context)