from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django import forms
import json, re

class new_task_form(forms.Form):
    task = forms.CharField(label="Add Task")

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "Todo/tasks.html",{
        "tasks": request.session["tasks"],
        "form": new_task_form()
    })

def add_task(request):
    if request.method == "POST":
        form = new_task_form(json.loads(request.body))
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
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
        del request.session["tasks"][index_li]
        request.session.modified = True
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)

def search_task(request):
    if request.method == 'POST':
        index_arr = []
        search_value = json.loads(request.body).get('search_value')
        reg = re.compile(f"^{search_value}")
        for i in range(len(request.session["tasks"])):
            if re.match(reg,request.session["tasks"][i]):
                index_arr.append(i)
        data = {
            'index_arr' : index_arr
        }
        return JsonResponse(data,status=200)
    else:
        return HttpResponse(status=500)


        
