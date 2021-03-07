from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/changepassword', user_views.change_password, name='change-password'),
    path('choose/',user_views.groups_choose, name = 'groups_choose'),
    path('delete/<str:group_id>',user_views.delete_group, name = 'delete'),
    path('grupy/',user_views.all_groups, name = 'all_groups'),
    path('aktywne/',user_views.active_groups, name = 'active_groups'),
    path('change/<str:snumber>',user_views.change_group, name = 'change_group'),
    path('grupy/<str:group_id>',user_views.all_students, name = 'group'),
    path('nowa_grupa',user_views.new_group, name = 'new_group'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('tests/', include('tests.urls')),
    path('', include('api.urls')),
    path('task/', include('upload.urls')),
    path('promela/', include('Promela.urls')),
    path('forum/', include('forum.urls')),
    path('captcha/', include('captcha.urls')),
]
