from rest_framework import serializers
from rest_framework.exceptions import NotFound

from .models import Reservation, ReservationItem
from items.serializers import ItemSerializer

class MyReservationItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ReservationItem
        fields = ('item',)

class MyReservationSerializer(serializers.ModelSerializer):
    items = MyReservationItemSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ("id","created_at","status","items",)

class ReservationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationItem
        fields = ('item',)

class ReservationSerializer(serializers.ModelSerializer):
    items = serializers.ListField(write_only=True, child=ReservationItemSerializer())

    class Meta:
        model = Reservation
        fields = ("id", "items",)

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        unavailable_items = []

        for item_data in items_data:
            item = item_data['item']
            if not item.available:
                unavailable_items.append(item)

        if unavailable_items:
            print(unavailable_items)
            raise NotFound(detail={"message": "Some items are unavailable", "unavailable_items": unavailable_items})

        reservation = Reservation.objects.create(**validated_data)

        for item_data in items_data:
            item = item_data['item']

            if item.available:
                item = item_data['item']
                item.available = False
                item.save()
                ReservationItem.objects.create(reservation=reservation, item=item)

            else:
                reservation.delete()  # Delete the reservation if any item is unavailable
                raise serializers.ValidationError(f"This item is unavailable: {item.title}")

        return reservation

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if instance.status == 'done' or instance.status == 'cancelled':
            reservation_items = instance.reservation_items.all()

            for reservation_item in reservation_items:
                item = reservation_item.item

                item.available  = True
                item.save()

        return instance