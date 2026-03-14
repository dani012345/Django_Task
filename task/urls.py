from django.urls import path
from . import views

urlpatterns = [
    # --- USERS ---
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # --- LISTS ---
    path('lists/', views.list_list, name='list_list'),
    path('lists/new/', views.list_create, name='list_create'),
    path('lists/<int:pk>/edit/', views.list_update, name='list_update'),
    path('lists/<int:pk>/delete/', views.list_delete, name='list_delete'),
    path('lists/my/', views.my_tasks, name='list_my'),

    # --- TASKS ---
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),

    # --- STARRED ---
    path('tasks/<int:pk>/star/', views.task_toggle_star, name='task_toggle_star'),
    path('tasks/starred/', views.starred_tasks, name='starred_tasks'),

    # --- EXTRA ---
    path('google/', views.go_to_google, name='go_to_google'),
]