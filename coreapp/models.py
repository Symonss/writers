# Here we are simply desghning how our database tables will look like
# class names translates to table names while fields become columns.
# functions inside classes give  actions that can be undertakent on these tables
from django.contrib.auth.models import AbstractUser
import random
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import escape, mark_safe

#oberriding the user class
class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    is_sub_admin = models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')
    #oder = models.ForeignKey(Order, on_delete=models.CASCADE, primary_key=True)

class SubAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')

class Service(models.Model):
    name = models.CharField(max_length=200)
    price_per_page = models.IntegerField()

    def __str__(self):
        return self.name

#  Order's table
class Order(models.Model):
    client = models.ForeignKey(Client, default=1, on_delete=models.CASCADE, related_name="orders")
    writer = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE, related_name="orders")
    order_topic = models.CharField(max_length=200,default="this is default", blank=True)
    order_description = models.TextField(blank=True,max_length=60)
    track_number = models.CharField(default="TRN-" +str(random.randrange(50050,5555505)),max_length=50)
    date_created = models.DateTimeField(blank=True,null=True,)
    deadline = models.DateTimeField(blank=True,null=True,)
    pages = models.IntegerField(blank=True,null=True,)
    price = models.IntegerField(default='500')
    words = models.IntegerField(default='50')
    document = models.FileField(upload_to='order_documents/' , blank=True,null=True,)
    is_available = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    is_editing = models.BooleanField(default = False)
    is_paid=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)
    service = models.OneToOneField(Service, on_delete=models.CASCADE, primary_key=True)

    def mark_available(self):
        if self.is_paid and self.is_approved:
            is_pending = False
            is_rejected = False
            is_available=True
        self.save()

    def mark_rejected(self):
        is_rejected= True
        self.save()


    def mark_approved(self):
        self.is_approved=True
        self.save()

    

    def __str__(self):
        return self.track_number



class Comment(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="comments")
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time=models.DateTimeField()
    is_seen=models.BooleanField(default=False)


class Bid(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="bids")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_amount=models.IntegerField()
