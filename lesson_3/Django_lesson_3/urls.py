
from django.contrib import admin
from django.urls import path

from managers.views import managers_view
from realty.views import realty_view
from request.views import request_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', realty_view),
    path('realty/', realty_view),
    path('managers/', managers_view),
    path('request/', request_view),
]
