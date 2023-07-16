from datetime import datetime

from django.test import TestCase

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer

# Create your tests here.
# class MenuItemTest(TestCase):
#     def test_get_item(self):
#         item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
#         self.assertEqual(str(item), "IceCream : 80")

# class BookingTest(TestCase):
#     def test_get_booking(self):
#         item = Booking.objects.create(name="Test", no_of_guests=1, booking_date=datetime.today().date())
        # self.assertEqual(str(item), "Test with 1, on 2023-07-15")

class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Beverage", price=10, inventory=100)
    def test_getall(self):
        getitems = MenuItem.objects.all()
        serializer = MenuItemSerializer(getitems)
        data = serializer.data
        self.assertEqual(data, {"IceCream : 80", "Beverage : 10"})