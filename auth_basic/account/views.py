from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    template_name='account/base.html'
    context={}
    return render(request,template_name,context)

def loginview(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p= request.POST.get('pw')
        user=authenticate(username=u,password=p)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponse('login successful')
        else:
            messages.error(request,'Invalid Credentials')
    template_name='account/log_in.html'
    context={}
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect('login')

def registerview(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            user_email=form.cleaned_data.get('email')
            messages.success(request,f'Account created for {username}!')
            send_mail(
                'Account Created',
                'Your Account has created succesful',
                'dawaresushma@gmail.com',
                [user_email],
                fail_silently=False
            )
    template_name='account/register.html'
    context={'form':form}
    return render(request,template_name,context)












