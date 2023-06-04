from django.contrib import admin

# Register your models here.
from django.contrib import admin
from request.models import Request


# Register your models here.
class RequestAdminView(admin.ModelAdmin):
    list_display = ('name', 'email', 'question')
    search_fields = ('name', 'email')


admin.site.register(Request, RequestAdminView)