from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('task/upload/',views.task_sended_upload),
    path('task/sendedList/',views.task_sended_list),
    path('task/',views.task, name='task'),
    path('forum/',views.forum),
    path('signup/', views.signup_view, name="signup"),
	path('login/',views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
]