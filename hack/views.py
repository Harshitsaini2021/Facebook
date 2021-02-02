from django.shortcuts import render
from .models import login
# Create your views here.

def index (request):
	if request.method=="POST": 
		email=request.POST.get("email","")
		password=request.POST.get("password","")
		Login=login(email=email, password=password)
		
		Login.save()
	return render(request,'index.html')
	
def error (request):
	return render(request,"error.html")	