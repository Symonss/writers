from django.contrib import admin
from .models import Order
from .models import Comment
# we register our objects here(these are the tables)
admin.site.register(Order)
admin.site.register(Comment)
