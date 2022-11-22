from . import views
from django.urls import path, reverse
from .views import BookingPage, get_data, edit_data, delete_data

urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
    path('home/', views.BookingList.as_view(), name='index'),
    path('overview/', get_data, name='overview'),
    path('edit/<data_id>', edit_data, name='edit'),
    path('delete/<data_id>', delete_data, name='delete'),
]
