from django.urls import path
#from crudapp.crud.todo.models import TodoApp
from .views import TodoAppCreateView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView, TodoAppDeleteView
from rest_framework.routers import DefaultRouter
from .views import TodoAppViewSet


router = DefaultRouter()
router.register(r'Todoapp=', TodoAppViewSet, basename='todoapp')

'''
urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list.html/', TodoAppListView.as_view()),
    path('detail/<pk>/', TodoAppDetailView.as_view()),
    path('<pk>/update', TodoAppUpdateView.as_view()),
    path('delete/<pk>', TodoAppDeleteView.as_view())

]
'''

urlpatterns = [] + router.urls

#127.0.0.1:8000/TodoApp