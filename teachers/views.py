from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Parent

def enroll_list(request):
    return render(request, 'enroll_list.html')


# add the parent in the teachers side
def parent_list(request):
    parents=Parent.objects.all()
    return render(request, 'parents/parent_list.html',{'parents':parents})


def add_parent(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        Parent.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
        messages.success(request, "Parent added successfully.")

        return redirect('parents')
    return render(request, 'parents/add_parent.html')


def update_parent(request,pk):
    parent=get_object_or_404(Parent,pk=pk)
    if request.method == 'POST':
        parent.first_name =request.POST.get('first_name') 
        parent.last_name =request.POST.get('last_name') 
        parent.phone_number =request.POST.get('phone_number') 
        parent.email =request.POST.get('email') 
        parent.save()

        messages.success(request, "Parent details updated successfully.")
        return redirect('parents')
    return render(request, 'parents/update_parent.html', {'parent':parent})

def delete_parent(request,pk):
    parent=get_object_or_404(Parent,pk=pk)
    if request.method == 'POST':
        parent.delete()
        messages.success(request, "Parent deleted successfully.")
        return redirect('parents')
    return render(request, 'parents/delete_parent.html',{'parent':parent})



