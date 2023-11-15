from django.contrib import admin


from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')
    inlines = [OrderItemInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
      if db_field.name == "order_items":
          kwargs["widget"] = admin.widgets.AdminRadioSelect
          kwargs["queryset"] = OrderItem.objects.none()
      return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        order = form.instance
        order_items = order.items.all()

        if order.status == 'done':
          for order_item in order_items:
              book = order_item.book
              book.available = True
              book.save()

admin.site.register(Order, OrderAdmin)
