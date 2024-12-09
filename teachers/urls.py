from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.enroll_list, name='enroll'),
    path('add_enroll/', views.add_enroll, name='enroll_child'),
    path('update_enroll/<int:pk>', views.update_enroll, name='update_enroll'),
    path('delete_enroll/<int:pk>', views.delete_enroll, name='delete_enroll'),
    
    path('parent_list/', views.parent_list, name='parents'),
    path('add_parent/', views.add_parent, name='add_parents'),
    path('update_parent/<int:pk>',views.update_parent,name='update_parent'),
    path('delete_parent/<int:pk>',views.delete_parent,name='delete_parent'),

    path('incident/', views.incident, name='incident'),
    path('add_incident/', views.add_incident, name='add_incidents'),
    path('update_incident/<int:pk>',views.update_incident, name='update_incident'),
    path('delete_incident/<int:pk>', views.delete_incident, name='delete_incident'),

    path('attendance/', views.attendance, name='attendance_list'),
    path('add_attendance/', views.add_attendance, name='add_attendances'),
    path('update_attendance/<int:pk>', views.update_attendance, name='update_attendance'),
    path('delete_attendance/<int:pk>', views.delete_attendance, name='delete_attendance'),
]