from django.db import reset_queries
from django.http import request
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from.models import post,Contact

# Create your views here.
def index(request):
    return render (request,'index.html')

def blog(request):
    posts= post.objects.all()
    return render(request,'blog.html',{'posts':posts})


def posts(request,pk):
    posts=post.objects.get(id=pk,)
    return render(request,'posts.html',{'posts':posts})
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')
    else:
        return render (request, 'register.html')


def login(request):
    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render (request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def Contact_view(request):
	if request.method == 'POST':
		form = Contact_view(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ('/')
      
	form = Contact_view()
	return render(request, "index.html", {'form':form})