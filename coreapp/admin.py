from django.contrib import admin
from .models import Order
# we register our objects here(these are the tables)
admin.site.register(Order)
