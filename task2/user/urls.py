
from django.urls import path
from .views import Register, Login, userView, Logout
from . import views

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/', userView.as_view()),
    path('logout/', Logout.as_view()),

    #task1
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('show/', views.show, name='show_tasks'),
]