from django.urls import path
from . import views

urlpatterns = [
    path("dynamic-form/", views.dynamic_form, name="dynamic_form"),
]