"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('threads/', views.ThreadListView.as_view(), name='threads'),
    path('threads/create/', views.ThreadCreateView.as_view(), name='thread-create'),
    path('threads/<int:pk>/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('threads/<int:pk>/delete/', views.ThreadDeleteView.as_view(), name='thread-delete'),
    path('threads/<int:pk>/edit/', views.ThreadUpdateView.as_view(), name='thread-edit'),
    path('threads/<int:pk>/post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
