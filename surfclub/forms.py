from django import forms
from .models import BookingCustomer, Booking


# class BookingCustomerForm(forms.ModelForm):
#     class Meta:
#         model = BookingCustomer
#         fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        # exclude = ('posted_by', 'approved')
