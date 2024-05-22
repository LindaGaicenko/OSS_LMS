from django.urls import path

from reservations import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('reservations/', views.ReservationList.as_view()),
]