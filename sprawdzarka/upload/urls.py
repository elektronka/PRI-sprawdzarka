from upload import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('upload/',views.task_student_sended_choose, name='upload'),
    path('uploadxml/', views.task_sended_upload, name='uploadxml'),

    path('tasklistchoose/', views.task_list_choose, name='task-list-choose'),
    path('taskuploadchoose/', views.task_upload_choose, name='task-upload-choose'),

    path('sendedtasks/<str:file_to_open>',views.read_file1, name='sended-task'),
    path('sendedlist/',views.task_sended_list, name='sended-list'),

    path('tasklist/',views.task_list, name='task-list'),
    path('tasklistupload/',views.task_List_upload, name='task-list-upload'),
    path('tasklist/<str:file_to_open>',views.read_file2, name='task-list-teacher'),

    path('tasksendedchoose/', views.task_sended_choose, name='task-sended-choose'),
    path('changepoints/<str:snumber_in_url>/<int:task_id_in_url>/',views.change_points_xml, name='change-points-xml'),
    path('changepoints/<str:snumber_in_url>/<int:task_id_in_url>/<str:number_task_in_url>',views.change_points_xml_direct, name='change-points-xml-direct'),

    path('plagiat',views.plagiat, name='plagiat'),
    path('plagiat/podglad/<str:file_to_open>', views.read_file1, name='open')
]

