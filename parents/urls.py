from django.urls import path
from . import views

urlpatterns = [
    path('child_infor/', views.child_infor, name="child_infor"),
    path('child_attendance/', views.child_attendace, name='child_attendance'),
    path('child_incident/', views.child_incident, name='child_incident'),
]

