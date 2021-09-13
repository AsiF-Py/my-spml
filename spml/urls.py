
from django.contrib import admin
from django.urls import path ,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('logout/', views.logout),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('certificates/', views.certificates),
    path('<slug>/<int:Code>/inquiry_item/', views.inquiry_item,name='inquiry_item'),
    path('login/', views.login),
    path('search/', views.search),
    path('<slug>/', views.product_list,name='products_category'),
    path('<slug>/<int:Code>/', views.product_detail,name='product_detail'),

]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)