from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,Category
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def products(request):
    deals=Products.objects.filter(category__name="deals")
    arrivals=Products.objects.filter(category__name="arrivals")
    Top=Products.objects.filter(category__name="Top")
    wifi=Products.objects.filter(category__name="wifi")
    return render (request,'product.html',{
        "deals":deals,
        "arrivals":arrivals,
        "Top":Top,
        "wifi":wifi,
    })
def product_detail(request,products_id):
   Product=get_object_or_404(Products,id=products_id)
   related_products = Products.objects.filter(
        category=Product.category
    ).exclude(id=Product.id)[:4]
   return render(request,"product_detail.html",{
       "Product":Product,
       "related_products":related_products 
   })
def add_to_cart(request, products_id):
    product = get_object_or_404(Products, pk=products_id)
    cart = request.session.get('cart', {})
    key = str(products_id)

    if key in cart:
        cart[key]['quantity'] += 1
    else:
        cart[key] = {
            'name': product.name,
            'image': product.image.url,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('products')
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    pk = str(pk)  # convert to string since session keys are strings

    if pk in cart:
        if cart[pk]['quantity'] > 1:
            cart[pk]['quantity'] -= 1
        else:
            del cart[pk]

    request.session['cart'] = cart
    return redirect('viewcart')  # or whatever your cart view name is

def get_cart_total(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return total

def cart_view(request):
    cart = request.session.get('cart', {})
    total=sum(item['price']* item['quantity'] for item in cart.values())
    return render(request, 'cart.html', { 
            "cart":cart, "total":total})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products") 
        else:
            messages.error(request, "Invalid username or password")
        return render(request, "login.html")
    return render(request, "login.html")
    
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()   # create the user
            login(request, user) # log them in immediately
            
           

            messages.success(request, "Account created successfully!")
            return redirect("products")  # change "home" to your home page url name
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", 
                  {"form": form})
@login_required
def profile(request):
    return render(request, "profile_list.html", {"user": request.user})