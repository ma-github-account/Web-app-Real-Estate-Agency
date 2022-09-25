from django.db import models
from django.urls import reverse


class Employee(models.Model):

	name = models.CharField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='employees/%Y/%m/%d', blank=True)
	mail = models.CharField(max_length=200, db_index=True)
	phone = models.DecimalField(max_digits=20, decimal_places=0)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'employee'
		verbose_name_plural = 'employees'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('agency:estate_list')

class Estate(models.Model):

	name = models.CharField(max_length=200)
	employee = models.ForeignKey(Employee, related_name='estates', on_delete=models.CASCADE)
	city = models.CharField(max_length=200, db_index=True)
	district = models.CharField(max_length=200)
	adress = models.CharField(max_length=200)
	image1 = models.ImageField(upload_to='estates/%Y/%m/%d', blank=True)
	image2 = models.ImageField(upload_to='estates/%Y/%m/%d', blank=True)
	image3 = models.ImageField(upload_to='estates/%Y/%m/%d', blank=True)
	area = models.DecimalField(max_digits=20, decimal_places=0)
	price = models.DecimalField(max_digits=20, decimal_places=0)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'estate'
		verbose_name_plural = 'estates'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('agency:estate_detail', args=[self.id])









