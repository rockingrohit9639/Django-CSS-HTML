from django.contrib import admin
from django.urls import path
from entry.views import home_view, contact_view, about_view, projects_view, search_view, events_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
	path('', home_view, name='home'),
	path('contact/', contact_view),
	path('projects/', projects_view),
	path('search/', search_view),
	path('events/', events_view),
	path('about/', about_view),
   	path('admin/', admin.site.urls),
   	path('product/', product_detail_view),
   	path('create/', product_create_view),
   	
]


