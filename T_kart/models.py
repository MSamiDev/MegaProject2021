from sre_parse import State
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now , datetime
from django.core.validators import MinLengthValidator



# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    product_slug = models.SlugField(
        max_length=300, editable=False, default=product_name, unique=True)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    discription = models.CharField(max_length=700)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="T-Kart/images/Products", default="")

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


class Customer(models.Model):
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50, )
    phone = models.CharField(max_length=15, )
    email = models.EmailField()
    password = models.CharField(max_length=500, )
    profile = models.ImageField(
        upload_to="T-Kart/images/Customer", default="T-Kart/images/Customer/default-image.jpg")


    def register(self):
        self.save()


    def __str__(self):
        return self.email

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    total_price = models.FloatField()
    company_name = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    address_line_1 = models.CharField(max_length=100, default='', blank=True)
    address_line_2 = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)
    pincode = models.IntegerField()
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateTimeField(default=now())
    transaction_id = models.AutoField
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
