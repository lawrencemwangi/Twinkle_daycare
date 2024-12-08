from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Parent
from authuser.models import CustomUser
from datetime import date
from .models import Enrollment


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
    return render(request, 'delete_confirm.html',{
        'item_type': 'Parent',
        'item_name': parent.first_name,
    })



# childern Enrollment logic
def enroll_list(request):
    enrolments=Enrollment.objects.all()
    return render(request, 'enrollment/enroll_list.html',{'enrolments':enrolments})


def add_enroll(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date') 
        gender = request.POST.get('gender')
        address = request.POST.get('address', '')
        admission_number = request.POST.get('admission_number')
        allergies = request.POST.get('allergies', '')
        medication = request.POST.get('medication', '')
        medical_conditions = request.POST.get('medical_conditions', '')
        emg_contact = request.POST.get('emg_contact')
        grade = request.POST.get('grade')
        parent_id = request.POST.get('parent')

        if not first_name or not last_name or not birth_date or not gender or not admission_number or not parent_id:
            parents = CustomUser.objects.filter(user_level='parent') 
            return render(request, 'enrollment/enrollment.html', {
                'error': 'All fields are required!',
                'parents': parents  
            })
        
        birth_date = date.fromisoformat(birth_date)
        today = date.today()

        parent = CustomUser.objects.get(id=parent_id)
        
        Enrollment.objects.create(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            address=address,
            admission_number=admission_number,
            allergies=allergies,
            medication=medication,
            medical_conditions=medical_conditions,
            emg_contact=emg_contact,
            grade=grade,
            parent=parent,
        )

        messages.success(request, "Child enrolled successfully.")
        return redirect('enroll')  
    
    else:
        parents = CustomUser.objects.filter(user_level='parent') 
 
 

def update_enroll(request,pk):
    enrollment = get_object_or_404(Enrollment,pk=pk)
    parents = CustomUser.objects.filter(user_level='parent')

    if request.method == 'POST':
        enrollment.first_name = request.POST.get('first_name')
        enrollment.last_name = request.POST.get('last_name')
        # enrollment.birth_date = request.POST.get('birth_date') 
        enrollment.gender = request.POST.get('gender')
        enrollment.address = request.POST.get('address', '')
        enrollment.admission_number = request.POST.get('admission_number')
        enrollment.allergies = request.POST.get('allergies', '')
        enrollment.medication = request.POST.get('medication', '')
        enrollment.medical_conditions = request.POST.get('medical_conditions', '')
        enrollment.emg_contact = request.POST.get('emg_contact')
        enrollment.grade = request.POST.get('grade')
        enrollment.parent_id = CustomUser.objects.get(id=request.POST.get('parent'))

        birth_date = request.POST.get('birth_date')
        if birth_date:
            enrollment.birth_date = date.fromisoformat(birth_date)
        # enrollment.parent_id = request.POST.get('parent')
        enrollment.save()
        messages.success(request, "Child enrollment updated successfully.")

        return redirect('enroll')
    return render(request, 'enrollment/update_enrollment.html', {'enrollment':enrollment,'parents': parents,})



def delete_enroll(request,pk):
    enrollment=get_object_or_404(Enrollment,pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, "Enrollment deleted successfully.")
        return redirect('enroll')
    return render(request, 'delete_confirm.html',{
        'item_type': 'Enrollment',
        'item_name': enrollment.first_name,
    })
        






