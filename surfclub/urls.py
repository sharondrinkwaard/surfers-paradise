from . import views
from django.urls import path
from .views import booking_page

urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('', views.booking_page, name='booking_page')
]
