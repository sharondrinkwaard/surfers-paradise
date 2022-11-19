from . import views
from django.urls import path, reverse
from .views import BookingPage

urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
    path('home/', views.BookingList.as_view(), name='index'),
    path('overview/', views.OverviewBookings.as_view(), name='overview/'),
]
