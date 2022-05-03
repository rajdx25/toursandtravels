from email import message
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from user.forms import Form
from user.models import Feedback
# Create your views here.
 
def home(request):
    return render(request,"user/base.html")

# def homes(request):
#     return render(request,'user/base.html')

def sign_up(request):
    if request.method =='POST':
        username =request.POST['username']
        password =request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            
            return render(request,'registration/login.html',{"message":"Invalid Credentials"})
            

    return render(request,'registration/login.html')

def logout(request):
    return redirect('registration/login.html')

def contactus(request):
    return render(request,'user/contactus.html')

def feedbackform(request):
    if request.method=='POST':
        add= Form (request.POST)
        if add.is_valid():

            # fname=add.cleaned_data['firstname']
            # lname=add.cleaned_data['lname']
            # email=add.cleaned_data['mailid']
            # country=add.cleaned_data['country']
            # feedback=add.cleaned_data['feedback']
            # fetch= Feedback(firstname=fname,lname=lname,mailid=email,country=country,feedback=feedback)
            add.save()
            add=Form()

            return redirect('base')
    else:
        add=Form()
    return render(request,'user/feedbackform.html',{'form':add})

# def store(request):
    
#     return render(request,'user/contactus.html',)
