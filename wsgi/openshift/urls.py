from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	    # Examples:
	    url(r'^$', 'views.home', name='home'),
	    #-------register,login & logout --------------------
	    url(r'^register/$','views.register'),
	    url(r'^login/$','views.login_view'),
	    url(r'^logout/$','views.logout_view'),
            #---------------------myorder &dashboard------------------------
	    url(r'^dashboard/$','views.dashboard'),
	    url(r'^myorder/$','views.myorders_view'),
            #------------------------------order-update url-----------------
	    url(r'^myorder/(?P<number>\d+)/$','views.order_update',name='order_update'),
	    
	    #-----------------------account change------------------------
	    	
	    url(r'^account/edit/$','views.account_edit'),

	   #----------------------redirect urls-------------------------------
	   url(r'^flipkart/$','views.flipkart_redirect'),




	    #--------------------------admin urls -----------------------
	    url(r'^admin/', include(admin.site.urls)),
	    #------------------------facebook-------------------------------
		 
	 
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
