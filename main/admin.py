from django.contrib import admin
from main.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def show_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.link, obj.link)

    show_link.allow_tags = True

    list_display = ('mark', 'model', 'body_type', 'year', 'announced_price', 'mileage', 'number_of_owners', 'phone_number', 'show_link', )
