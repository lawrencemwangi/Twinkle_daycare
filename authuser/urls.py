from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'), 
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('parent/', views.parent_dashboard, name='parent_dashboard'),
    # path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]
