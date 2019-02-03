from django.contrib import admin

from .models import (User, Client, SubAdmin)
# we register our objects here(these are the tables)
admin.site.register(Client)
admin.site.register(SubAdmin)
admin.site.register(User)
