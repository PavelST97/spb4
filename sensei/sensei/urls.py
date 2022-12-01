from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
]
