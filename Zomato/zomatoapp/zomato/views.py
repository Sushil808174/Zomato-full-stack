from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm,OrderForm,MenuItemForm
from .models import UserProfile,MenuItem,Order
from django.urls import reverse

def home(request):
    data = MenuItem.objects.all()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request,username=username,password=password)
        if auth is not None:
            login(request,auth)
            messages.success(request,"You have been logged In!")
            return redirect('home')
        else:
            messages.success(request,"There was an error Logging in, Please try again...")
            return redirect('home')
    else:    
        return render(request,'home.html',{'data':data})


def register(request):
    if request.method == 'POST':
        print("this is inside register")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('data saved')
            # Save additional fields to UserProfile
            UserProfile.objects.create(
                user=user,
                name=form.cleaned_data['username'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            auth = authenticate(username=username, password=password)
            login(request, auth)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = RegistrationForm()
        print('not valid')
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request,"You have been Logged out...")
    return redirect('home')

def item_details(request,item_id):
    if request.user.is_authenticated:
        item = MenuItem.objects.get(id=item_id)
        user = request.user
        # print(user.username)
        return render(request,'item_detail.html',{'item':item,'user':user}) 
    else:
        messages.success(request,"You must be logged In...")
        return redirect('home')

def go_place_order(request,item_id):
    place_order_url = reverse('place_order', kwargs={'item_id': item_id})
    return redirect(place_order_url)


def place_order(request, item_id):
    if request.user.is_authenticated:
        item = MenuItem.objects.get(id=item_id)
        
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
            if quantity is not None:
                quantity = int(quantity)
                total_price = item.price * quantity
                Order.objects.create(
                    user=request.user,
                    item=item,
                    quantity=quantity,
                    total_price=total_price
                )
                messages.success(request, "Ordered successfully...")
                # return render(request, 'order_success.html')
                return redirect( 'home')
        
        # Render the template with the item
        return render(request, 'place_order.html', {'item': item})
    else:
        messages.success(request, "You must be logged in to place an order.")
        return redirect('home')

def myorders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'myorder.html', {'orders': orders})
    else:
        messages.success(request, "You must be logged in to view your orders.")
        return redirect('home')


@login_required
def profile(request):
    user_profile = request.user.userprofile
    return render(request, 'profile.html', {'user_profile': user_profile})


def order_success(request):
    return render(request,'order_success')


@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu item added successfully.')
            return redirect('home')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

@login_required
def update_menu_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu item updated successfully.')
            return redirect('home')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'update_menu_item.html', {'form': form, 'item': item})    