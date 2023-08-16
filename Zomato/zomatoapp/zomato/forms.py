from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile,MenuItem  # Import your UserProfile model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),label="")
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),label="")
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone no.'}),label="")
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),label="")
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),label="")
    state = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),label="")
    pincode = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pincode'}),label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modify widgets for password fields
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password1'].label = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
        self.fields['password2'].label = ''

    class Meta:
        model = User
        fields = ['username','name', 'email', 'password1', 'password2', 'phone', 'address', 'city', 'state', 'pincode']


class OrderForm(forms.Form):
    item = forms.ChoiceField(choices=[])  # Replace with actual choices
    quantity = forms.IntegerField(min_value=1)