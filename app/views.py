from django.shortcuts import render , HttpResponseRedirect , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import QCCertificates , product
from django.db.models import Q
from .forms import Inquiry_form , SignUpForm , ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail , BadHeaderError
from django.template.loader import render_to_string, get_template
from django.views.generic import ListView , DetailView
from django.urls import resolve

def home(request):
	return render(request,'home.html')
	
def product_list(request,slug):
	pro_list = product.objects.filter(Products_Category=slug)
	return render(request,'product.html',{'pro_list':pro_list} ) 

def product_detail(request,slug,Code):
	context ={}
	context["list"]  = product.objects.get(Code = Code)
	return render(request,'product_detail.html',context) 


def login(request):
	return render(request,'login.html')

def logout(request):
	return render(request,'registration/logout.html')

def signup_view(request):

	form=SignUpForm()

	if request.method=='POST':

		form=SignUpForm(request.POST)

		user=form.save()

		user.set_password(user.password)

		user.save()

		return HttpResponseRedirect('/accounts/login')

	return render(request,'signup.html',{'form':form})

def search(request):
	name = request.GET.get('query')
	pro = product.objects.filter(Q(Products_Name__contains=name)|Q(Code__contains=name))
	return render(request,'search.html',{'pro':pro,'name':name})    

def inquiry_item(request,slug,Code):
	data  = product.objects.filter(Code = Code)
	sent=False
	form = Inquiry_form()
	if request.method=='POST':
		form=Inquiry_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			subject='{} know about ({}) '.format(cd['name'],cd['product_name'])
			text1 = cd['name']
			text2 = cd['product_name']
			text3 = cd['product_code']
			text4 = cd['Address']
			text5 = cd['Country']
			text6 = cd['comments']
			c = {'text1': text1,'text2': text2,'text3': text3,'text4': text4,'text5': text5,'text6': text6}
			html_content = render_to_string('mail.html', c)
			txtmes = render_to_string('mail.html', c)
			send_mail(subject,txtmes,cd['to'],['asifuddin1152@gmail.com'],html_message=html_content)
			sent=True
			messages.success(request, 'Your Email Send Successful')
		else:
			form=Inquiry_form()
			messages.success(request, 'Email Send Fail')

				

	return render(request,'inquiry_item.html',{'form':form,'data':data})


def certificates(request):
	search = False
	if 'query' in request.GET:
		query = request.GET['query']
		mycertificate = QCCertificates.objects.filter(Batch__exact=query)
		search = True
	else:
		mycertificate = ""
	context = {
		'queryset' : mycertificate,'search':search
	}

	return render(request,'certificates.html',context)


def contact(request):
	if request.method=="POST":
			email = request.POST['email']
			message = request.POST['message']
			subject = request.POST['subject']
			send_mail(
   subject,                    #Subject here
	   message,                    #Here is the message.
		email ,     # from mail
	   ['asifuddin1152@gmail.com'],  #spml mail / email
		# fail_silently=False,                  
)    
	return render(request,'contact.html')


def about(request):
	return render(request,'about.html')
	
def home(request):
	return HttpResponse("hello")