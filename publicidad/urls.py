"""publicidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Registration of new users
    path('register/', views.RegistrationView.as_view()),

    # Todos endpoint
    path('todos/', views.TodosView.as_view()),
    path('todos/(^P<todo_id>[0-9]*)', views.TodosView.as_view()),

    # API authentication
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
