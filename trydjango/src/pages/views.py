from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from templates.forms import CreateUserForm #importing the form that i have created in templates/forms
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
    #url.py from Singhealth project will look at the page.views or any other app views u creeated
def contact_view(*args,**kwargs):
    return HttpResponse("<h1> Testing </h1>")
def login_view (request,*args,**kwargs):
    if request.user.is_authenticated :
        return redirect('dashboard')
    else:
        if request.method == 'POST':
        #submitting a form
            user_name =request.POST.get('username')#get from login.html username
            user_password = request.POST.get('password')#get from login.html password
            user=authenticate(request,username=user_name,password=user_password)# authenticating the user credentials
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request , 'Invalid Username or Password')

        return render (request,'login.html',{})
def logout_view(request):
    logout(request)
    return redirect('login')
    ##logout which wil return the person to the login page    

def register_view(request):
    if request.user.is_authenticated :
        return redirect('dashboard')
    
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)#render the form again
            if form.is_valid():#validating the form        
                form.save()#save the user form ,creating the user
                messages.success(request,'Your account has been created successfully !')
                return redirect('login')


        context={'form':form}
        return render(request,'register.html',context)
@login_required(login_url='login') ##any views that can only be accessed via login is guarded by this decorator
def dashboard_view(request):
    return render(request,'dashboard.html',{})
    #this restricts any person who hasnt login to access the dashboard with the decorator applied


@login_required(login_url='login')
def search_view(request):
    tenant = tenants.objects.all()



    context = {'tenant':tenant}

    return render(request ,'search.html',context)
