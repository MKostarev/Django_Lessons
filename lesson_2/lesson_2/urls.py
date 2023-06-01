
from django.contrib import admin
from django.urls import path

from product_list.views import list_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_product),
]
