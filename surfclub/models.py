from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms


ALL_CHOICES = (
    ('Beginner Surf Lesson', 'Beginner Surf Lesson'),
    ('Intermediate Surf Lesson', 'Intermediate Surf Lesson'),
    ('Surf Coaching', 'Surf Coaching'),
    ('Kids Camp', 'Kids Camp'),
)

TIME_CHOICES = (
    ('10:00', '10:00'),
    ('12:00', '12:00'),
    ('14:00', '14:00'),
    ('16:00', '16:00'),
    ('18:00', '18:00'),
)


class Booking(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    options = models.CharField(max_length=80, choices=ALL_CHOICES, default='Beginner Surf Lesson')
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default='10:00')
    notes = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    # booking_nr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Name: {self.first_name, self.last_name} | Email: {self.email} | Date: {self.date} | Time {self.time} | Notes: {self.notes}'


class BookingCustomer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default='10:00')
    options = models.CharField(max_length=80, choices=ALL_CHOICES, default='Beginner Surf Lesson')
    notes = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'Name: {self.first_name, self.last_name} | Date: {self.date} | Time {self.time} | Notes: {self.notes} | Option: {self.options}'
