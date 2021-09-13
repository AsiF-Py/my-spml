from django import forms
from .models import *
from django_countries.fields import CountryField
from django import forms
from django.contrib.auth.models import User
class Inquiry_form(forms.Form):
	product_name=forms.CharField()
	product_code=forms.CharField()
	name=forms.CharField()
	Address=forms.CharField()
	Country=forms.CharField()
	to=forms.EmailField()
	comments=forms.CharField(required=True,widget=forms.Textarea)



class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']	


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
