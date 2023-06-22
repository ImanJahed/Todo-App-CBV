from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm


# Create your views here.
class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoCreateView(CreateView):
    form_class = TodoForm
    template_name = 'todo/todo_list.html'
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = 'title',
    template_name = 'todo/todo_list.html'
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo-list')


def todo_finish(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.status = True
    todo.save()
    return redirect('todo-list')