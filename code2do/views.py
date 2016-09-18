from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect	
from django.views.decorators.csrf import csrf_protect
from models import Users, Problems
from django.db import IntegrityError
import re

@csrf_protect
def index(request):
	try:
		if request.session["isloggedin"] == True:
			return HttpResponseRedirect("/profile")
	except KeyError:
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
		user = Users.objects.get(email=request.POST['email'])
		expected_password = user.password
		hash_pass = hash(request.POST['password'])
		if hash_pass == expected_password or request.POST["fb"] == "1":
			request.session["isloggedin"] = True
			request.session["email"] = user.email
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
	handle = request.POST['handle']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	try:
		user = Users(email=email, handle=handle, first_name=first_name, last_name=last_name, password=hash_pass)
		user.save()
		request.session["isloggedin"] = True
		request.session["email"] = email
		return HttpResponse("1")
	except IntegrityError:
		return HttpResponse("0")

@csrf_protect
def profile(request):
	try:
		if request.session["isloggedin"] == True:
			email = request.session["email"]
			return render(request, "profile.html", {"user_email": email})
	except KeyError:
		context = {}
		return HttpResponseRedirect("/")

@csrf_protect
def logout(request):
	try:
		if request.session["isloggedin"] == True:
			del request.session["isloggedin"]
			del request.session["email"]
		return HttpResponseRedirect("/")
	except KeyError:
		return HttpResponseRedirect("/")

@csrf_protect
def addproblem(request):
	try:
		problem_url = request.POST["problem_url"]
		print problem_url + "Here"
		if "codechef.com" in problem_url and re.search("problems/[A-Z0-9]", problem_url):
			site = "codechef"
		elif "hackerearth.com" in problem_url and "/algorithm/" in problem_url:
			site = "hackerearth"
		elif "hackerrank.com" in problem_url and "/challenges/" in problem_url:
			site = "hackerrank"
		elif "codeforces.com" in problem_url and "/problem/" in problem_url:
			site = "codeforces"
		elif "spoj.com" in problem_url and re.search("problems/[A-Z0-9]", problem_url):
			site = "spoj"
		else:
			return HttpResponse("Invalid Url")
		email = request.session["email"]
		user = Users.objects.get(email=email)
		problem = Problems(user=user, site=site, url=problem_url, name=problem_url)
		problem.save()
		return HttpResponse("Problem successfully added to todo list")
	except KeyError:
		return HttpResponseRedirect("/")

@csrf_protect
def codechef(request):
	user = Users.objects.get(email=request.session["email"])
	problem_list = Problems.objects.filter(site="codechef", user=user)
	return render(request, "todolist.html", {"problem_list": problem_list, "site":"Codechef"})

@csrf_protect
def codeforces(request):
	user = Users.objects.get(email=request.session["email"])
	problem_list = Problems.objects.filter(site="codeforces", user=user)
	return render(request, "todolist.html", {"problem_list": problem_list, "site":"Codeforces"})
	
@csrf_protect
def hackerearth(request):
	user = Users.objects.get(email=request.session["email"])
	problem_list = Problems.objects.filter(site="hackerearth", user=user)
	return render(request, "todolist.html", {"problem_list": problem_list, "site":"Hackerearth"})
	
@csrf_protect
def hackerrank(request):
	user = Users.objects.get(email=request.session["email"])
	problem_list = Problems.objects.filter(site="hackerrank", user=user)
	return render(request, "todolist.html", {"problem_list": problem_list, "site":"Hackerrank"})
	
@csrf_protect
def spoj(request):
	user = Users.objects.get(email=request.session["email"])
	problem_list = Problems.objects.filter(site="spoj", user=user)
	return render(request, "todolist.html", {"problem_list": problem_list, "site":"Spoj"})
	