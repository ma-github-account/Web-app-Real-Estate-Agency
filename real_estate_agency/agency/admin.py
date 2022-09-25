from django.contrib import admin
from .models import Employee, Estate

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

	list_display = ['name']

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
	
	list_display = ['name', 'employee', 'city','price']




















