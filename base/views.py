from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import  Order,Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, ProductForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
@login_required
def home(request):
    return render(request,"home.html",{"name":"test"})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tv_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    
    return render(request, 'add_order.html', {'form': form})

@login_required
def tv_list_view(request):
    tvs = Product.objects.all()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return render(request,'listeproduct.html',{"tvs":tvs,'form': form})
    else:
        form = ProductForm()
        return render(request, 'listeproduct.html', {"tvs":tvs,'form': form})


@login_required
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'listecommandes.html', {'orders': orders})

@login_required
def delete_order_view(request, id):
    tv = Order.objects.get(id=id)
    tv.delete()
    return redirect('order_list')

@login_required
def edit_tv_view(request, id):
    tv =Product.objects.get(id=id)
    if request.method == 'POST':
        tv.name = request.POST['name']
        tv.qte = request.POST['qte']
        tv.price = request.POST['price']
        tv.save()
        return redirect('tv_list')
    return render(request, 'myapp/edit_tv.html', {'tv': tv})

@login_required
def delete_tv_view(request, id):
    tv = Product.objects.get(id=id)
    tv.delete()
    return redirect('tv_list')

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('tv_list')  # Redirect to product list page
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form})

def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Redirect to order list page
    else:
        form = OrderForm(instance=order)
    return render(request, 'add_product.html', {'form': form})
