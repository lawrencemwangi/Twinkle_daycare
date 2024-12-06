from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.urls import reverse

# Create your views here.

# class CustomLoginView(LoginView):
#     template_name = 'login.html'  # Path to your login template

#     def form_valid(self, form):
#         # Get the logged-in user
#         user = form.get_user()
#         login(self.request, user) 

#         # Redirect user based on their user_level
#         if user.user_level == 'admin':
#             return HttpResponseRedirect('/admin/dashboard/') 
#         elif user.user_level == 'teacher':
#             return HttpResponseRedirect('/teacher/dashboard/')  
#         elif user.user_level == 'parent':
#             return HttpResponseRedirect('/parent/dashboard/')  
#         else:
#             return HttpResponseRedirect('/') 

# admin
def admin_dashboard(request):
    if request.user.user_level != 'admin':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, '/admin') 

# Teacher Dashboard
def teacher_dashboard(request):
    if request.user.user_level != 'teacher':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'dashboard/teacher_dashboard.html') 

# Parent Dashboard
def parent_dashboard(request):
    if request.user.user_level != 'parent':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'dashbard/parent_dashboard.html') 


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        next_url = self.request.GET.get('next', '/')

        # Redirect based on user level
        if user.user_level == 'admin':
            return redirect('admin:index') 
        elif user.user_level == 'teacher':
            return HttpResponseRedirect(f'/teacher{next_url}')
        elif user.user_level == 'parent':
            return HttpResponseRedirect(f'/parent{next_url}')
        else:
            return HttpResponseRedirect(next_url)
