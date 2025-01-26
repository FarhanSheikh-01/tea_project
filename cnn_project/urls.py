from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('myapp.urls')),
    path("introduction/", include('myapp.urls')),
    path("composition/", include('myapp.urls')),
    path("fertilizers/", include('myapp.urls')),
    path("practices/", include('myapp.urls')),
]
