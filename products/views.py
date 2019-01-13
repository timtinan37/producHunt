from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
	products = Product.objects
	return render(request,'products/home.html', {'products': products})

def create(request):
	if not request.user.is_authenticated:
		return render(request,'accounts/login.html', {'error': 'You must login first!'})
	else:
		if request.method == 'POST':
			if request.POST['title'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon'] and request.POST['body']:
				product = Product()
				product.title = request.POST['title']
				product.body = request.POST['body']
				if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
					product.url = request.POST['url']
				else: 
					product.url = 'http://' + request.POST['url']
				product.icon = request.FILES['icon']
				product.image = request.FILES['image']
				product.pub_date = timezone.datetime.now()
				product.hunter = request.user
				product.save()
				return redirect('/products/' + str(product.id))
			else:
				return render(request,'products/create.html', {'error': 'All the fields are required!'}) 
		else:
			return render(request, 'products/create.html')	
	
    
def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/detail.html', {'product': product})


def upvote(request, product_id):
	if request.method == 'POST':
		if not request.user.is_authenticated:
			return render(request,'accounts/login.html', {'error': 'You must login first!'})
		else:
			product = get_object_or_404(Product, pk=product_id)
			product.votes_total += 1
			product.save()
			return redirect('/products/' + str(product.id))
