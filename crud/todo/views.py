from struct import pack
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoApp
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import TodoAppSerializer


class TodoAppCreateView(CreateView):
    model = TodoApp
    fields = [
        "title",
        "description"
    ]
    template_name = 'home.html'
    success_url = 'list.html'

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

def index(request):
    context = {
        "todo" : "posts"
    }
    return JsonResponse(context)

class TodoAppViewSet(viewsets.ModelViewSet):
    queryset = TodoApp.objects.all()
    serializer_class = TodoAppSerializer
#you can add this
#payload = {
#    "title" : "Holiday",
#    "description" : "It's time to rest"
#}
#TodoApp.objects.create(title=payload["title"], description=payload["description"])