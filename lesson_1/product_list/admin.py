from django.contrib import admin

from product_list.models import Food

# Register your models here.
class FoodAdminView(admin.ModelAdmin):
    list_display = ('name', 'intro', 'info', 'id')

admin.site.register(Food, FoodAdminView)