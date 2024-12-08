from django.shortcuts import render
from teachers.models import Enrollment

# Create your views here.

def child_infor(request):
    parent = request.user

    children = Enrollment.objects.filter(parent=parent)

    if not children:
        return render(request, 'children/children_infor.html', {'error': 'No children found for this parent.'})

    return render(request, 'children/children_infor.html', {'children': children})
