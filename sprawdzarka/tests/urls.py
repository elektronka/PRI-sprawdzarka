from django.urls import path
from .views import *

urlpatterns = [
    path('', tests_home, name = 'tests_home'),
    path('new/', new_test, name = 'new_test'),
    path('all/', all_tests, name = 'all_tests'),
    path('<int:test_id>/<int:question_id>', test, name='test' ),
    path('confirm/<int:test_id>', confirm_test, name = 'confirm_test'),
    path('end/<int:test_id>', end_test, name = 'end_test')
]