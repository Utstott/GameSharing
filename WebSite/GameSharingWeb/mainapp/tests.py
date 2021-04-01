from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Notebook, CartProduct, Cart, Customer
from decimal import Decimal
from .views import recalc_cart

User = get_user_model()


class ShopTestCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='Notebooks')
        image = SimpleUploadedFile("media/AN.jpg", content=b'1', content_type="image/jpg")
        self.notebook = Notebook.objects.create(
            category=self.category,
            title="Test Nootebook",
            slug="test-slug",
            image=image,
            price=Decimal('50000.00'),
            diagonal="17.3",
            display_type="IPS",
            processor_freq="3.4 GHz",
            ram="6 Gb",
            video="GeForce GTX",
            time_without_charge="10 H"
        )
        self.customer = Customer.objects.create(user=self.user, phone="11111", address="ADDRR")
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.notebook
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('50000.00'))
