from django.contrib import admin

# Register your models here.
from django.contrib import admin
from product_list.models import Food, Category


# Register your models here.
class FoodAdminView(admin.ModelAdmin):
    list_display = ('name', 'intro', 'id', 'cat')
    search_fields = ('intro', 'name')
    list_display_links = ('name', 'intro')
    ordering = ('id', 'name')


admin.site.register(Food, FoodAdminView)
admin.site.register(Category)