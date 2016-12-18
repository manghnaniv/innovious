from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about_us.html')

def products(request):
	return render(request,'products/products.html')
	
def true_hb(request):
	return render(request,'products/true_hb.html')
	
def true_hb_strip(request):
	return render(request,'products/true_hb_strip.html')	
	
def health_areas(request):
	return render(request,'health_areas/index.html')		
	
def anaemia(request):
	return render(request,'health_areas/anaemia.html')		
	
def breast_cancer(request):
	return render(request,'health_areas/breast_cancer.html')
	
def career(request):
	return render(request,'careers/index.html')
	
def hr(request):
	return render(request,'careers/hr.html')
	
def receptionist(request):
	return render(request,'careers/receptionist.html')				
	
def delivery_boy(request):
	return render(request,'careers/delivery_boy.html')
	
def account_executive(request):
	return render(request,'careers/account_executive.html')
	
def sales_executive(request):
	return render(request,'careers/sales_executive.html')		
	
def contact_us(request):
	return render(request,'contact_us.html')
	
	
