from django.contrib import admin
from .models import Category, Event, EventSession, Booking

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(EventSession)
admin.site.register(Booking)    

# Register your models here.
