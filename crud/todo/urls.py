from django.urls import path
from .views import TodoAppCreateView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView, TodoAppDeleteView


urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view()),
    path('detail/<pk>/', TodoAppDetailView.as_view()),
    path('<pk>/update', TodoAppUpdateView.as_view()),
    path('delete/<pk>', TodoAppDeleteView.as_view())

]
