from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'time', 'email', 
                    'created_on', 'approved')
    search_fields = ['first_name', 'last_name', 'date', 'email']
    list_filter = ('date', 'approved')
    summernotes_fields = ('content')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
