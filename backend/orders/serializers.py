from rest_framework import serializers
from rest_framework.exceptions import NotFound

from .models import Order, OrderItem
from books.serializers import BookSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = OrderItem
        fields = ('book',)

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id","created_at","status","items",)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('book',)

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(write_only=True, child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ("id", "items",)

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        unavailable_books = []

        for item_data in items_data:
            book = item_data['book']
            if not book.available:
                unavailable_books.append(book)

        if unavailable_books:
            print(unavailable_books)
            raise NotFound(detail={"message": "Some books are unavailable", "unavailable_books": unavailable_books})

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            book = item_data['book']

            if book.available:
                book = item_data['book']
                book.available = False
                book.save()
                OrderItem.objects.create(order=order, book=book)

            else:
                order.delete()  # Delete the order if any book is unavailable
                raise serializers.ValidationError(f"This book is unavailable: {book.title}")

        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if instance.status == 'done':
            order_items = instance.order_items.all()

            for order_item in order_items:
                book = order_item.book

                book.available  = True
                book.save()

        return instance