from rest_framework import serializers

from .models import Category, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "title",
            "author",
            "description",
            "publisher",
            "publication_date",
            "available",
            "get_image",
            "get_file",
            "file_url",
            "is_external"
        )

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "type",
            "title",
            "author",
            "slug",
            "publication_date",
            "get_absolute_url",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "name",
            "description",
            "get_absolute_url",
            "items",
        )