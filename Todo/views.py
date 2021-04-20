from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django import forms
import json

class new_task_form(forms.Form):
    task = forms.CharField(label="Add Task")

# Create your views here.

tasks = []

def index(request):
    return render(request, "Todo/tasks.html",{
        "tasks": tasks,
        "form": new_task_form()
    })

def add_task(request):
    if request.method == "POST":
        form = new_task_form(json.loads(request.body))
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            print("Task Added")
            data ={'added': True}
        else:
            print("Some error occured")
            data ={'added': False}
        return JsonResponse(data,status=200)
    else:
        return HttpResponse(status=200)

def delete_task(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        index_li = request_data.get('index')
        del tasks[index_li]
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)

        
