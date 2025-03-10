from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]