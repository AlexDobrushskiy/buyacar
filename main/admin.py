from django.contrib import admin
from main.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'body_type', 'year', 'mileage', 'number_of_owners', 'phone_number', 'link',)
