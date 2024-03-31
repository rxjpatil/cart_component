# views.py

from django.shortcuts import render
from .models import Employee
from django.http import Http404

def employee_detail(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")
    
    return render(request, 'employee_detail.html', {'employee': employee})
