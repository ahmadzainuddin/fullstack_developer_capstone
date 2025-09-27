from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "type", "year", "dealer_id")
    list_filter = ("car_make", "type", "year")
    search_fields = ("name", "car_make__name")


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "country")
    search_fields = ("name",)
    inlines = [CarModelInline]
