from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking, BookingCustomer
from .forms import BookingForm


class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'


# class GetData(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('-created_on')
#     template_name = 'overview.html'


def get_data(request):
    current_user = request.user
    queryset = Booking.objects.filter(posted_by=current_user)
    context = {'queryset': queryset}

    return render(request, 'overview.html', context)


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


def delete_data(request, data_id):
    data = get_object_or_404(Booking, id=data_id)
    data.delete()
    return redirect('overview')


# Class to make bookings
class BookingPage(View):

    def get(self, request):
        template_name = 'booking.html'
        form = BookingForm()
        context = {'form': form}

        return render(request, template_name, context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.posted_by = request.user
            form.save()
            return redirect('booking')


class OverviewBookings(View):

    def get(self, request):
        queryset = Booking.objects
        # booking = get_object_or_404(queryset)
        booking_overview = OverviewBookings(data=request.GET)
        # booking_overview.instance.first_name = request.user.first_name
        # booking_overview.instance.last_name = request.user.last_name
        # booking_overview.instance.email = request.user.email
        # booking_overview.instance.date = request.user.date
        # booking_overview.instance.time = request.user.time
        # booking_overview.instance.options = request.user.options
        # booking_overview.instance.notes = request.user.notes

        return render(request, 'overview.html')


# class SubmitForm(View):

#     def submit(self, request, *args, **kwargs):
#         queryset = BookingCustomer.objects
#         submit = get_object_or_404(queryset)
#         submit_form = SubmitForm(data=request.POST)
#         if submit_form.is_valid():
#             submit_form.instance.first_name = request.user.first_name
#             submit_form.instance.last_name = request.user.last_name
#             submit_form.instance.email = request.user.email
#             submit_form.instance.date = request.user.date
#             submit_form.instance.time = request.user.time
#             submit_form.instance.options = request.user.options
#             submit_form.instance.notes = request.user.notes
#             customer_booking = submit_form.save(commit=False)
#             customer_booking.post = submit
#             customer_booking.save()
#         else: 
#             submit_form = SubmitForm()

#         return render(request, 'booking.html')
