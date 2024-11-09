from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('show/', views.show, name='show_tasks'),
]