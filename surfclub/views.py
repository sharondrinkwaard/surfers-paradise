from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


# Gets the index template and imports the main booking model
class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'


# Filters the data by the authenticated user and displays the users bookings
def get_data(request):
    current_user = request.user
    queryset = Booking.objects.filter(posted_by=current_user)
    context = {'queryset': queryset}
    # if no booking: html: You have no bookings yet
    return render(request, 'overview.html', context)


# Function to edit data; displays the form incl the previous data
def edit_data(request, data_id):
    data = get_object_or_404(Booking, id=data_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=data)
        if form.is_valid():
            form.save(commit=False)
            form.posted_by = request.user
            form.save()
            return redirect('overview')
    form = BookingForm(instance=data)
    context = {'form': form}
    return render(request, 'edit_data.html', context)


# Function to delete a booking
def delete_data(request, data_id):
    data = get_object_or_404(Booking, id=data_id)
    data.delete()
    return redirect('overview')


# Class to make bookings; displays and posts the form
class BookingPage(View):

    def get(self, request):
        template_name = 'booking.html'
        form = BookingForm()
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.posted_by = request.user
            booking.save()
            return redirect('overview')
        else:
            render(request, 'booking.html', {'form': form})
