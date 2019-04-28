from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Todo
from datetime import datetime


def test_view(request):
    return HttpResponse('ok')


def todo_list(request):
    todos = Todo.objects.filter().order_by('created_date')
    return render(request, 'todo_list.html', {'todos': todos})


"""
get_todo_list
"""
def get_todo_list(request):
    todos = Todo.objects.all()
    todos_obj = {'todos_list': []}
    for todo in todos:
        todos_obj['todos_list'].append({
                'pk': todo.pk,
                'text': todo.text,
                'completed': todo.completed,
                'created_date': todo.created_date.strftime("%m/%d/%Y %I:%M:%S %p")
        })
    return JsonResponse(todos_obj)


"""
add_todo
"""
def add_todo(request):
    if request.method == "POST":
        request_text = request.POST.get('todoInput')
        if not (request_text == "Enter a new task.." or request_text == ''):
            td = Todo(text=request_text)
            td.save()
            print("Created New To-Do: " + request_text)
            return HttpResponse('OK')
    else:
        return HttpResponse('Non-Accepted Method')

# toggle_todo

def toggle_todo(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(id=pk)
        if (todo):
            todo.toggle_complete()
            return HttpResponse("OK")
        else:
            return HttpResponse("Item not found.")


# delete_todo


def delete_todo(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(id=pk)
        if (todo):
            todo.delete()
            return HttpResponse("OK")
        else:
            return HttpResponse("Item not found.")
