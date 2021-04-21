from django.urls import path
from . import views

app_name = "Todo"
urlpatterns =[
    path("", views.index, name="index"),
    path("addtask", views.add_task, name="addtask"),
    path("deletetask", views.delete_task, name="deletetask"),
    path("search", views.search_task, name="searchtask")
]