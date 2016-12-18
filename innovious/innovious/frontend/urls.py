from django.conf.urls import url, include

from frontend.views import *

urlpatterns = [
	url(r'^$',index),	
	url(r'^about_us/$',about),
	url(r'^products/$',products),
	url(r'^products/true_hb/$',true_hb),
	url(r'^products/true_hb_strip/$',true_hb_strip),
	url(r'^health_areas/$',health_areas),
	url(r'^health_areas/anaemia/$',anaemia),
	url(r'^health_areas/breast_cancer/$',breast_cancer),
	url(r'^career/$',career),
	url(r'^career/hr/$',hr),
	url(r'^career/receptionist/$',receptionist),
	url(r'^career/sales_executive/$',sales_executive),
	url(r'^career/delivery_boy/$',delivery_boy),
	url(r'^career/account_executive/$',account_executive),
	url(r'^contact_us/$',contact_us),
	

]
