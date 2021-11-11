from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse, BadHeaderError
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings


def signup_view(request):
    if request.method=='POST':
        u=request.POST.get('username')
        f=request.POST.get('Fname')
        l= request.POST.get('Lname')
        e = request.POST.get('email')
        ph= request.POST.get('phone')
        p1= request.POST.get('password')
        p2= request.POST.get('password-repeat')
        obj=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p1)
        obj.save()
        subject='Welcome to Healthify World'
        message=f'Hi{obj.username},Thank you for registering'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[obj.email]
        send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        messages.success(request,'sucessful')
        if p1!=p2:
           return HttpResponse('p1 and p2 should be same')
        return redirect('log_in')
    template_name='Account/register1.html'
    context={}
    return render(request,template_name,context)

def login_view(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p= request.POST.get('password')
        print(f'username entered-{u},Password enterd={p}')
        user = authenticate(username=u, password=p)
        print(user)
        if user is not None:
            login(request,user)
            '''
            send_mail(
                'Account Created ',
                'Your Account has created succesfully .'
                'Your ID and Password is safe with us'
                'Thank you for Registration',
                'dawaresushma@gmail.com',
                [user.email],
                fail_silently=False,
            )
            '''
            return redirect('navbar')
        else:
            messages.error(request,'Invalid Credentials')
    template_name = 'Account/log_in.html'
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('log_in')
