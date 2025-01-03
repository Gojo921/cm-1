from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter
from django .contrib.auth.forms import UserCreationForm
from django .contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from decorators import unauthenticated_user


@unauthenticated_user
def register(request):
        form = Createuserform()  

        if request.method == "POST":
            form = Createuserform(request.POST)  
            if form.is_valid(): 
                form.save()  

                return redirect('login') 
        
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'Username OR Password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)

def logout__view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')

def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    
    
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def accountsettings(request):
    customer = request.user.customers
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
        CustomerForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
    context = {'form': form}
    
    return render(request, 'accounts/accounts_settings.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products} )


def customers(request,pk):
   customer = Customers.objects.get(id=pk)
   orders = customer.order_set.all()

   order_count = orders.count()
   myFilter = OrderFilter(request.GET, queryset=orders)
   orders = myFilter.qs
   context = {'customer': customer, 'orders': orders, 'order_count':order_count, 'myFilter': myFilter}
   return render(request, 'accounts/customers.html', context )

@login_required(login_url='login')
def createOrder(request, pk):
   
    OrderFormSet = inlineformset_factory(Customers, Order, fields=('product', 'status'), extra=10 )
    
   
    customer = Customers.objects.get(id=pk)

  
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/') 

   
    context = {
        'formset': formset,
    }
    
    return render(request, 'accounts/order_form.html', context)  

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) 
    
    if request.method == 'POST':  
        form = OrderForm(request.POST, instance=order)  
        
        if form.is_valid():  
            form.save() 
            return redirect('/')  
    
    context = {'form': form}  
    return render(request, 'accounts/order_form.html', context)  


@login_required(login_url='login')
def DeleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method   == "POST":
        order.delete()
        return redirect('/')
         
    context = {'item': order}
    return render(request, 'accounts/remove.html', context)





