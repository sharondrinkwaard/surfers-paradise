from . import views
from django.urls import path
from .views import BookingPage

urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
]
