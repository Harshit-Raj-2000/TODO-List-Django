from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class new_task_form(forms.Form):
    task = forms.CharField(label="Add Task")

# Create your views here.

tasks = ['foo', 'bar', 'baz', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tenetur eligendi reprehenderit cum corrupti. Eligendi placeat voluptate illo alias fugiat ullam, dolorum cupiditate voluptatum sit consequatur, iure a facilis molestiae ab!']

def index(request):
    return render(request, "Todo/tasks.html",{
        "tasks": tasks,
        "form": new_task_form()
    })

