from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoApp
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class TodoAppCreateView(CreateView):
    model = TodoApp
    fields = [
        "title",
        "description"
    ]
    template_name = 'home.html'
    success_url = "list.html"

class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'list.html'

class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'detail.html'

class TodoAppUpdateView(UpdateView):
    model = TodoApp
    fields =[
        "title",
        "description"
    ]
    template_name = 'update.html'
    success_url = '/'

class TodoAppDeleteView(DeleteView):
    model = TodoApp
    template_name = 'delete.html'
    success_url = '/'