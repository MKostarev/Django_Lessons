from django.contrib import admin

# Register your models here.
from django.contrib import admin
from managers.models import Managers


# Register your models here.
class ManagersAdminView(admin.ModelAdmin):
    list_display = ('name', 'telefon')
    search_fields = ('name', 'telefon')


admin.site.register(Managers, ManagersAdminView)