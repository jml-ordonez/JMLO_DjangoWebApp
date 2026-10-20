from django.urls import path
from . import api_views

urlpatterns = [
    path(
        'students/',
        api_views.api_student_list,
        name='api_student_list'
    ),
]