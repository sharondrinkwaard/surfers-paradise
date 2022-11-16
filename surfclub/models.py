from django.db import models
from django.contrib.auth.models import User
from django import forms

ALL_CHOICES = (
    ('1', 'Beginner Surf Lesson - No experience'),
    ('2', 'Intermediate Surf Lesson - 5 > lessons'),
    ('3', 'Surf Coaching - 2 hours')
    ('4', 'Surf Coaching - 4 hours')
    ('5', 'Kids Camp')
)


class Booking(model.Models):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='#')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    # options = forms.MultipleChoiceField(choices=ALL_CHOICES)
    notes = models.TextField(blank=True)
    # status = approved / not approved
    # booking_nr = 

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.customer

