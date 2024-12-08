from django.urls import path
from . import views

urlpatterns = [
    path('child_infor', views.child_infor, name="child_infor")
]

