# Here we are simply desghning how our database tables will look like
# class names translates to table names while fields become columns.
# functions inside classes give  actions that can be undertakent on these tables

from django.conf import settings
from django.db import models
from django.utils import timezone

# Order's table
class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_topic = models.CharField(max_length=200, blank=True)
    order_description = models.TextField(blank=True)
    track_number = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    date_created = models.DateTimeField()
    deadline = models.DateTimeField()
    is_available = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_editing = models.BooleanField(default = False)
    order_files = models.CharField(max_length=200, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.order_topic
