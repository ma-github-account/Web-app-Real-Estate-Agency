from django.shortcuts import render, get_object_or_404
from .models import Employee, Estate

def estate_list(request):

	employee = None
	employees = Employee.objects.all()
	estates = Estate.objects.all()
	return render(request, 'agency/estate/list.html', {'employee': employee, 'employees': employees, 'estates': estates})

def estate_detail(request, id):

	estate = get_object_or_404(Estate, id=id)
	return render(request, 'agency/estate/detail.html', {'estate': estate})








