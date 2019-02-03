from django.contrib import admin

from .models import (User,Status, Order, Comment, Bid, Client, SubAdmin)
# we register our objects here(these are the tables)
admin.site.register(Client)
admin.site.register(SubAdmin)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Bid)
