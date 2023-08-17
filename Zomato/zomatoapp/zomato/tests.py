from django.test import TestCase
from .models import UserProfile,MenuItem,Order
from django.contrib.auth.models import User

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='susheel',password='12345')
        self.profile = UserProfile.objects.create(
            user=self.user,
            name='Susheel Kumar',
            email='sushil@gmail.com',
            phone='1234567890',
            address='Banki',
            city='Hamirpur',
            state='Uttar Pradesh',
            pincode='123456'
        )
    def test_user_profile_creation(self):
        self.assertEqual(self.profile.user.username,'susheel')
        self.assertEqual(self.profile.name,'Susheel Kumar')
        self.assertEqual(self.profile.email,'sushil@gmail.com')
        self.assertEqual(self.profile.phone,'1234567890')
        self.assertEqual(self.profile.address,'Banki')
        self.assertEqual(self.profile.city,'Hamirpur')
        self.assertEqual(self.profile.state,'Uttar Pradesh')

class MenuItemModelTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            name='Dosha',
            image='dosha.jpg',
            price=10.99,
            availability=True
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.item.name, 'Dosha')
        self.assertEqual(self.item.price, 10.99)

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='susheel', password='password')
        self.item = MenuItem.objects.create(
            name='Pizza',
            image='pizza.jpg',
            price=99,
            availability=True
        )
        self.order = Order.objects.create(
            user=self.user,
            item=self.item,
            quantity=2,
            total_price=198,
            status='pending'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'susheel')
        self.assertEqual(self.order.item.name, 'Pizza')
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_price, 198)
        self.assertEqual(self.order.status, 'pending')      