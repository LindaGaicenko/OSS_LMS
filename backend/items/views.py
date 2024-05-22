from django.db.models import Q
from django.http import Http404

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters import rest_framework as filters

from .models import Item, ItemFilter, Category
from .serializers import ItemSerializer, ItemListSerializer, CategorySerializer

class LatestItemsList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()[0:4]
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetail(APIView):
    def get_object(self, category_slug, item_slug):
        try:
            return Item.objects.filter(category__slug=category_slug).get(slug=item_slug)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, item_slug, format=None):
        item = self.get_object(category_slug, item_slug)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class FilterData(RetrieveAPIView):
     def get(self, *args, **kwargs):
        items = Item.objects.all()
        authors = {item.author for item in items}
        publishers = {item.publisher for item in items}
        result = ({"authors": authors, "publishers": publishers})

        return Response(result) or Response([])

class ItemsList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_class = ItemFilter



@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query == '':
        items = Item.objects.all()
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)
    elif query:
        items = Item.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query))
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response({"items": []})