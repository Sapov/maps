from django.contrib import admin
from django.urls import path, include

from .views import InfoListView

urlpatterns = [
    path('', InfoListView.as_view(), name='gh'),
]
