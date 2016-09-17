from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from models import Users, Problems
from django.db import IntegrityError

@csrf_protect
def index(request):
	context = {}
	return render(request, "index.html", context)

def hash(password):
	hash_pass = 0
	base = 31
	mod = 10e9+7
	for i in range(len(password)):
		hash_pass = (hash_pass*31 + ord(password[i])+1)%mod
	return str(hash_pass)


@csrf_protect
def checkvalidity(request):
	valid = 0
	try:
		expected_password = Users.objects.get(email=request.POST['email'])
		hash_pass = hash(request.POST['password'])
		if hash_pass == expected_password:
			return HttpResponse("1")
		else:
			return HttpResponse("0")
	except Users.DoesNotExist:
		return HttpResponse("0")

@csrf_protect
def register(request):
	email = request.POST["email_register"]
	first_name = request.POST["first_name_register"]
	last_name = request.POST["last_name_register"]
	return render(request, "register.html", {"email":email, "first_name":first_name, "last_name":last_name})

@csrf_protect
def add_new_user(request):
	hash_pass = hash(request.POST['password'])
	email = request.POST['email']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	try:
		user = Users(email=email, first_name=first_name, last_name=last_name, password=hash_pass)
		user.save()
		return HttpResponse("1")
	except IntegrityError:
		return HttpResponse("0")