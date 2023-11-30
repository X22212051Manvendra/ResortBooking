"""My Resort Booking Project"""
from django.contrib import admin
from .models import Resorts, Rooms, Reservation

# Register your models here.
admin.site.register(Resorts)
admin.site.register(Rooms)
admin.site.register(Reservation)
