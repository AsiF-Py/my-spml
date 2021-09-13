from django.db import models
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager
from django.utils.text import slugify 
Products_Type_CHOICES = [
	('our products', 'Our Products'),
	('product-industry', 'Product-Industry'),

]


Products_Category_CHOICES = [
	('Our Products', (
			('agar_plates', 'Agar Plates'),
			('bi_agar_plates_90mm', 'Bi Agar Plates 90mm'),
			('agar_plates_150mm', 'Agar Plates 150mm'),
			('tubed_media', 'Tubed Media'),
			('bottled_media', 'Bottled Media'),
			('blood_products', 'Blood Products'),
			('antibiotic_discs', 'Antibiotic Discs'),
			('aTCC-Microbiologic', 'ATCC-Microbiologic'),
			('petroleum', 'Petroleum'),
		)
	),
	('Product-Industry', (
			('clinical', 'Clinical'),
			('cosmetic', 'Cosmetic'),
			('dairy', 'Dairy'),
			('food', 'Food & Beverage'),
			('veterinary', 'Veterinary'),
			('Water_Wastewater', 'Water & Wastewater'),
		)
	),
	('unknown', 'Unknown'),
]

	

class product(models.Model):
	Products_Name = models.CharField(max_length=100)
	Code = models.IntegerField(unique=True)
	Product_Description = models.TextField(default='')
	Products_Attachment = models.FileField(upload_to='file', max_length=100,default='')
	Products_Image = models.ImageField(upload_to='images', max_length=100,default='')
	Products_Type  = models.CharField(choices=Products_Type_CHOICES,max_length=100,default='')
	Products_Category = models.CharField(choices=Products_Category_CHOICES,max_length=100,default='')
	slug=models.SlugField(default='',help_text = "Products Category and slug are must be same.")
	Indended_Use = TaggableManager(help_text = "Tag")
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.Products_Category)
		super(product, self).save(*args, **kwargs)
		
	def  __str__(self):
		 return '{} | {}'.format(self.Products_Name, self.Code)
	class Meta:
		ordering = ('Code',)
		verbose_name = 'Product'
		verbose_name_plural = 'Products'
	def get_absolute_url(self):
		reverse('products_category',args=[self.slug])
	def get_absolute_url(self):
		reverse('product_detail',args=[self.slug,self.Products_Name])	 
		 

class QCCertificates(models.Model):
	Products_Name = models.OneToOneField(product,on_delete=models.CASCADE)
	Batch = models.IntegerField()
	Plant = models.CharField(max_length=50)
	Products_Attachment = models.FileField(upload_to='QCCertificates/file',default='')
	Expiry_date = models.DateField(auto_now=False, auto_now_add=False)
	def  __str__(self):
		 return 'QCCertificates {}'.format(self.Batch)
	class Meta:
		verbose_name = 'QC Certificate'
		verbose_name_plural = 'QC Certificates'



	
	
  


  
  
