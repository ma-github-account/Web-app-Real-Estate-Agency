from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
	path('', views.estate_list, name='estate_list'),
	path('<int:id>', views.estate_detail, name='estate_detail'),
]






























