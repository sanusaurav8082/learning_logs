# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def logout_view(request):
	"""Log the user out."""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	"""Register a new user."""
	if request.method!='POST':
		#Display the blank registration form
		form=UserCreationForm()
	else:
		#Process the completed form
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user=form.save()
			#log the user in and then redirect to the homepage
			authenticated_user=authenticate(username=new_user.username,
			password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context={'form':form}
	return render(request,'users/register.html',context)

def loginit(request):
	"""Register a new user."""
	if request.method!='POST':
		form=AuthenticationForm()
		#Display the blank registration form
	else:
		#Process the completed form
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log the user in and then redirect to the homepage
			authenticated_user=authenticate(username=form.cleaned_data.get('username'),
			password=form.cleaned_data.get('password'))
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context={'form':form}
	return render(request,'users/login.html',context)

