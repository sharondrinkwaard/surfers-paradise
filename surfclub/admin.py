from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'time', 'email')
    search_fields = ['first_name', 'last_name', 'date', 'email']
    list_filter = ('date',)  # sorts bookings by date
    summernotes_fields = ('content')
