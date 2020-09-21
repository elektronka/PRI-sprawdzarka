"""sprawdzarka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api import views
from upload import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('upload/',views.task_sended_upload, name='upload'),
    path('sendedtasks/<str:file_to_open>',views.read_file1, name='sended-task'),
    path('sendedlist/',views.task_sended_list, name='sended-list'),
    path('tasklist/',views.task_list, name='task-list'),
    path('tasklistupload/',views.task_List_upload, name='task-list-upload'),
    path('tasklist/<str:file_to_open>',views.read_file2, name='task-list-teacher'),
]

