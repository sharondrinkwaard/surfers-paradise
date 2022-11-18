from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking, BookingCustomer
from .forms import BookingCustomerForm


class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'


class BookingPage(View):

    def get(self, request):
        template_name = 'booking.html'
        form = BookingCustomerForm()
        context = {'form': form}

        return render(request, template_name, context)

    def post(self, request):
        form = BookingCustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.posted_by = request.user
            form.save()
            return redirect('booking')


class SubmitForm(View):

    def submit(self, request, *args, **kwargs):
        queryset = BookingCustomer.objects
        submit = get_object_or_404(queryset)
        submit_form = SubmitForm(data=request.POST)
        if submit_form.is_valid():
            submit_form.instance.first_name = request.user.first_name
            submit_form.instance.last_name = request.user.last_name
            submit_form.instance.email = request.user.email
            submit_form.instance.date = request.user.date
            submit_form.instance.time = request.user.time
            submit_form.instance.options = request.user.options
            submit_form.instance.notes = request.user.notes
            customer_booking = submit_form.save(commit=False)
            customer_booking.post = submit
            customer_booking.save()
        else: 
            submit_form = SubmitForm()

        return render(request, 'booking.html')
