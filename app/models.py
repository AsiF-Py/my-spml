from django.db import models
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager
from django.utils.text import slugify 

Products_Category_CHOICES = [

			('agarplates', 'Agar Plates'),
			('biagarplates', 'Bi Agar Plates 90mm'),
			('150biagarplates', 'Agar Plates 150mm'),
			('tubedmediabroths', 'Tubed Media'),
			('bottledmedia', 'Bottled Media'),
			('bloodproducts', 'Blood Products'),
			('antibioticdiscs', 'Antibiotic Discs'),
			('atcc', 'ATCC-Microbiologic'),
			('petroleum', 'Petroleum'),

]

	

class product(models.Model):
	Code = models.CharField(unique=True,max_length=100,blank=True,null=True)
	Products_Name = models.CharField(max_length=100,blank=True,null=True)
	

	Product_Description = models.TextField(default='')

	Products_Attachment = models.FileField(max_length=100,default='',blank=True,null=True)

	Products_Image = models.ImageField(max_length=100,default='',blank=True,null=True)
	
	Products_Category = models.CharField(choices=Products_Category_CHOICES,max_length=100,default='',blank=True,null=True)



	slug=models.SlugField(default='hello',help_text = "Products Category and slug are must be same.",blank=True,null=True)

	Indended_Use = TaggableManager(help_text = "Tag",blank=True)
	
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



	
	
  


  
  
