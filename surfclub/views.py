from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'
