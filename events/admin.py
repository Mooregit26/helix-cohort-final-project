
from django.contrib import admin
from .models import Category, Event, EventSession, Booking


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'location', 'organizer')
    list_filter = ('category',)
    search_fields = ('title', 'location')


@admin.register(EventSession)
class EventSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'date', 'start_time', 'end_time', 'capacity')
    list_filter = ('date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_reference', 'user', 'session', 'status')
    list_filter = ('status',)
    search_fields = ('booking_reference', 'user__username')