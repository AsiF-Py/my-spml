
from django.contrib import admin
from django.urls import path ,include
from app import views
from django.views.static import serve 

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('logout/', views.logout),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('certificates/', views.certificates),
    path('<slug>/<Code>/inquiry_item/', views.inquiry_item,name='inquiry_item'),
    path('login/', views.login),
    path('search/', views.search),
    path('<slug>/', views.product_list,name='products_category'),
    path('product_industry/<tag_slug>/', views.Indended_Use_product_list,name='product_industry'),
    path('<slug>/<Code>/', views.product_detail,name='product_detail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
 #       urlpatterns += static(settings.MEDIA_URL,
  #                            document_root=settings.MEDIA_ROOT)
