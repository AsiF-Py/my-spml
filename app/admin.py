from django.contrib import admin
from .models import *


from django.shortcuts import render , HttpResponseRedirect

@admin.register(product)
class productAdmin(admin.ModelAdmin):
	list_display = ['Products_Name','Code','Indended_Use','Products_Category',]
	list_filter=('Code','Products_Category')
	prepopulated_fields={'slug':('Products_Category',)}
	search_fields = ('Products_Name','Code')
	list_editable = ('Indended_Use', )
	actions = ['update_sulg']
	def update_sulg(self, request, queryset):
		if 'apply' in request.POST:
			for obj in queryset:
				obj.slug = obj.Products_Category
				obj.save()
		return render(request,'admin/pub.html',context={'product':queryset})
	update_sulg.short_description = "Update Slug"




@admin.register(QCCertificates)
class productAdmin(admin.ModelAdmin):
	list_display = ['Products_Name','Batch','Plant','Expiry_date',]
	list_filter=('Products_Name','Batch','Plant')
	search_fields = ('Products_Name','Batch','Plant') 

