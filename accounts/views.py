from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
	if request.method=='POST':
		# User has info and wants an account now!
		try:
			if request.POST['password1']==request.POST['password2']:
				user = User.objects.get(username=request.POST['Username'])
				return render(request,'accounts/signup.html', {'error': 'Username already exists! Try again with a different one.'})
			else:
				return render(request,'accounts/signup.html',{'error': "Passwords MUST match."})
		except User.DoesNotExist:
			user = User.objects.create_user(username=request.POST['Username'],
											password=request.POST['password1'])
			return render(request,'accounts/login.html',{'success': 'User successfully created.'})
	else:
		# User wants to enter info
		return render(request,'accounts/signup.html')

def login(request):
	if request.method=='POST':
		user = auth.authenticate(username=request.POST['Username'],
								 password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request,'accounts/login.html', {'error': 'Username or Password is incorrect.'})
	else:
		return render(request, 'accounts/login.html')
def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect('home')
	