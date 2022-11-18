from django import forms
from .models import BookingCustomer


class BookingCustomerForm(forms.ModelForm):
    class Meta:
        model = BookingCustomer
        fields = '__all__'
