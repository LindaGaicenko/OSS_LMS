from django.urls import path, include

from items import views

urlpatterns = [
    path('latest-items/', views.LatestItemsList.as_view()),
    path('items/search/', views.search),
    path('items/filter', views.FilterData.as_view()),
    path('items/', views.ItemsList.as_view()),
    path('items/<slug:category_slug>/<slug:item_slug>/', views.ItemDetail.as_view()),
    path('items/<slug:category_slug>/', views.CategoryDetail.as_view()),
]