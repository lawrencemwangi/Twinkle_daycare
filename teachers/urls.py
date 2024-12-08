from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.enroll_list, name='enroll'),
    path('add_enroll/', views.add_enroll, name='enroll_child'),
    
    path('parent_list/', views.parent_list, name='parents'),
    path('add_parent/', views.add_parent, name='add_parents'),
    path('update_parent/<int:pk>',views.update_parent,name='update_parent'),
    path('delete_parent/<int:pk>',views.delete_parent,name='delete_parent'),


]