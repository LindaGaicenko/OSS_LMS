from django.contrib.auth.models import User
from django.db import models

from items.models import Item

class Reservation(models.Model):
    STATUS_OPTIONS = [
        ('new', 'New'),
        ('active', 'Active'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=20, choices=STATUS_OPTIONS, default='new')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.id}"

class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.item.title