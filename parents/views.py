from django.shortcuts import render,redirect
from teachers.models import Enrollment,Attendance,Incident

# Create your views here.

def child_infor(request):
    parent = request.user

    children = Enrollment.objects.filter(parent=parent)

    if not children:
        return render(request, 'children/children_infor.html', {'error': 'No children found for this parent.'})

    return render(request, 'children/children_infor.html', {'children': children})


def child_attendace(request):
    parent = request.user

    children = Enrollment.objects.filter(parent=parent)

    attendances = Attendance.objects.filter(child__in=children)

    if not attendances.exists():
        return render(request, 'children/children_attendance.html', {'error': 'No child attendance details found'})
        print(attendances)

    return render(request, 'children/children_attendance.html', {'attendances': attendances})


def child_incident(request):
    parent = request.user

    children = Enrollment.objects.filter(parent=parent)

    incidents = Incident.objects.filter(child__in=children)

    
    if not incidents.exists():
        return render(request, 'children/children_incident.html', {'error': 'No child attendance details found'})
        print(attendances)

    return render(request, 'children/children_incident.html', {'incidents': incidents})