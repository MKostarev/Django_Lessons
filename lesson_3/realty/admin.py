from django.contrib import admin

# Register your models here.
from django.contrib import admin
from realty.models import Realty, Category


class RealtyAdminView(admin.ModelAdmin):
    list_display = ('name', 'adres', 'info', 'cat', 'id')
    search_fields = ('name', 'adres')
    list_display_links = ('name', 'adres')


admin.site.register(Realty, RealtyAdminView)
admin.site.register(Category)