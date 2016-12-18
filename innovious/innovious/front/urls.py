from django.conf.urls import url, include
ffrom frontend.views import index

urlpatterns = [
	url(r'/',index),	
]
