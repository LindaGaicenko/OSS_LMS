from django.contrib import admin
from .models import Reservation, ReservationItem

class ReservationItemInline(admin.TabularInline):
    model = ReservationItem
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')
    inlines = [ReservationItemInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
      if db_field.name == "reservation_items":
          kwargs["widget"] = admin.widgets.AdminRadioSelect
          kwargs["queryset"] = ReservationItem.objects.none()
      return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        reservation = form.instance
        reservation_items = reservation.items.all()

        if reservation.status == 'done':
          for reservation_item in reservation_items:
              item = reservation_item.item
              item.available = True
              item.save()

admin.site.register(Reservation, ReservationAdmin)
