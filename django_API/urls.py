from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('data_API_App.urls')),
    path('shop/', include('data_API_App.urls')),
]
