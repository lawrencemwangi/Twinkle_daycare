from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home , name='home'),
    path('about/', views.About , name='about_page'),
    path('service/', views.Service , name='service_page'),
    path('contact/', views.Contact , name='contact_page'),  
]
