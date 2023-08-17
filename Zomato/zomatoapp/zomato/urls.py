from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('item_details/<int:item_id>', views.item_details, name='item_details'),
    path('go_place_order/<int:item_id>', views.go_place_order, name='go_place_order'),
    path('place_order/<int:item_id>', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('myorders/',views.myorders,name='myorders'),
    path('profile/', views.profile, name='profile'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('update_menu_item/<int:item_id>/', views.update_menu_item, name='update_menu_item'),
]