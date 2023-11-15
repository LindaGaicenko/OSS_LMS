from django.contrib.auth.models import User
from django.db import models

from books.models import Book

class Order(models.Model):
    STATUS_OPTIONS = [
        ('new', 'New'),
        ('active', 'Active'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=20, choices=STATUS_OPTIONS, default='new')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.book.title