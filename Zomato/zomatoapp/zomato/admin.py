from django.contrib import admin
from .models import UserProfile,MenuItem,Order
admin.site.register(UserProfile)
admin.site.register(MenuItem)
admin.site.register(Order)