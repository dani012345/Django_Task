from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),

    # Lists
    path('lists/', views.list_list, name='list_list'),
    path('lists/new/', views.list_create, name='list_create'),

    # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),

    # Google redirect
    path('google/', views.go_to_google, name='go_to_google'),
]