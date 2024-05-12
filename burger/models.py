from typing import Tuple

from django.contrib.auth import get_user_model
from django.db import models

LABEL_CHOICES = (
    ('S', 'sale'),
    ('N', 'new'),
    ('P', 'promotion')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Burger(models.Model):
    name = models.CharField(max_length=125)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='burgers')
    gram = models.IntegerField()
    photo = models.ImageField(upload_to='uploads/products/')
    about = models.TextField()
    price = models.IntegerField(default=0)
    digital = models.BooleanField(default=False, null=True, blank=False)
    published_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Presintation(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='presintation/% Y/% m/% d/')
    published_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Burger, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([li.cost() for li in self.lineitem_set.all()])


class Payment(models.Model):
    PAYPAL_PAYMENT_METHOD = 'PayPal'
    PAYMENT_METHODS = (
        (PAYPAL_PAYMENT_METHOD, 'PayPal'),
    )

    client = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.client}"


class StripePayment(models.Model):
    amount = models.FloatField(default=0)
    successful = models.BooleanField(default=False)
    payment_intent_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(
        to=CartItem,
        on_delete=models.CASCADE,
        related_name='stripe_payments',
    )

    def __str__(self) -> str:
        return self.reference_number

    @property
    def reference_number(self) -> str:
        return f"STRIPE-PAYMENT-{self.order}-{self.pk}"
