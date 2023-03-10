from django.shortcuts import render, redirect
from .models import Tugas
from .forms import TugasForm
from django.contrib.auth import authenticate, login

def home(request):
    tasks = Tugas.objects.all()
    form = TugasForm()

    if request.method == "POST":
        form = TugasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        "tasks" : tasks,
        "form" : form
    } 
    return render(request, "tugas/home.html", context) 


def updateTask(request, pk):
    task = Tugas.objects.get(id=pk)
    form = TugasForm(instance=task)

    if request.method == "POST":
        form = TugasForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context = {
            'form' : form
    }

    return render(request, "tugas/update.html", context,)


def delete(request, pk):
    item = Tugas.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    context = {
        'item' : item,
    }

    return (request, "tugas/delete.html", context)

def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render(request, "tugas/csrf.html",ctx)
