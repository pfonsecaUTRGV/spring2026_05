#Add the forms for our models 
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Task


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model= Profile
		fields = ['bio','student_id','enrolled']


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title','completed']


