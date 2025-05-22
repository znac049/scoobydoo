"""
URL configuration for Scooby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from Doo.views import HomePage, TapeListView, TapeCreateView, TapeUpdateView, TapeDeleteView

urlpatterns = [
    path('', HomePage.as_view()),
    path('admin/', admin.site.urls),
    path('tapes/', TapeListView.as_view(), name='tape-list'),
    path('tapes/add/', TapeCreateView.as_view(), name='tape-add'),
    path('tapes/<int:pk>/', TapeUpdateView.as_view(), name='tape-update'),
    path('tapes/<int:pk>/delete/', TapeDeleteView.as_view(), name='tape-delete'),
]
