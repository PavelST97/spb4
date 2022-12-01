from django.urls import path

from .views import PersonList

urlpatterns = [
    path('ooo/', PersonList.as_view()),
]
