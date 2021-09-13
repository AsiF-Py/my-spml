from django.contrib import admin
from .models import *




@admin.register(product)
class productAdmin(admin.ModelAdmin):
	list_display = ['Products_Name','Code','Products_Type','Products_Category',]
	list_filter=('Products_Name','Code','Products_Type','Products_Category')
	prepopulated_fields={'slug':('Products_Category',)}
	search_fields = ('Products_Name','Code')




@admin.register(QCCertificates)
class productAdmin(admin.ModelAdmin):
	list_display = ['Products_Name','Batch','Plant','Expiry_date',]
	list_filter=('Products_Name','Batch','Plant')
	search_fields = ('Products_Name','Batch','Plant') 

