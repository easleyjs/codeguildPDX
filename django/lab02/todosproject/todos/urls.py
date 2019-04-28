from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
        path('', views.todo_list, name='todo_list'),
        path('add/', views.add_todo, name='add_todo'),
        path('list/', views.get_todo_list, name='get_todo_list'),
        path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
        path('toggle/<int:pk>/', views.toggle_todo, name='toggle_todo'),
]
