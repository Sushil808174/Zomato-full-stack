from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm,OrderForm
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
    print("inside place-ordeer")
    if request.user.is_authenticated:
        print("inside auth")
        item = MenuItem.objects.get(id=item_id)
        print('after item')
        if request.method == 'POST':
            print("inside post")
            quantity = request.POST['quantity']
            total_price = item.price * quantity
            print(total_price)
            Order.objects.create(
                user=request.user,
                item=item,
                quantity=quantity,
                total_price=total_price
            )
            messages.success(request, "Ordered successfully...")
            return redirect('order_success')
    else:
        print('outside auth')
        messages.success(request, "You must be logged in to place an order.")
        return redirect('home')




def order_success(request):
    return render(request,'order_success')