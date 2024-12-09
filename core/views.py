from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_page')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'contact.html')
    