from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from datetime import datetime
from home.models import create
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')

def solvepage(request):
    return render(request,'solve.html')

def loginuser(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/solve")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")
            
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/")



def contact(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pss1=request.POST['pss1']
        pss1=request.POST['pss1']
        

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pss1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/login')
    
    return render(request,'create.html')
   