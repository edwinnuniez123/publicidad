from django.contrib import admin
from .models import Brand, Store, Deal, User, User_store

admin.site.register(Brand)
admin.site.register(Store)
admin.site.register(Deal)
admin.site.register(User)
admin.site.register(User_store)
# Register your models here.
