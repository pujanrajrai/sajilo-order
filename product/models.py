from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Product(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveBigIntegerField()

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=(
                                                        ('created', 'Created'),
                                                        ('paid', 'Paid'),
                                                        ('shipped', 'Shipped'),
                                                        ('delivered', 'Delivered'),
                                                        ('cancelled', 'Cancelled')),
                                                        default='created'
                                                        )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=255, choices=(
                                                                ('credit_card', 'Credit Card'),
                                                                ('debit_card', 'Debit Card'),
                                                                ('net_banking', 'Net Banking'),
                                                                ('wallet', 'Wallet'),
                                                                ('upi', 'UPI'),
                                                                ('cod', 'Cash on Delivery')),
                                                                default='credit_card'
                                                                )
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=(
                                                        ('success', 'Success'),
                                                        ('failed', 'Failed'),
                                                        ('pending', 'Pending')),
                                                        default='pending'
                                                        )
