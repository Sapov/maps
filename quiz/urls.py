from django.contrib import admin
from django.urls import path, include

from .views import InfoListView, question, check_answer, quantity

app_name = 'quiz'


urlpatterns = [
    path('', InfoListView.as_view(), name='allinfo'),
    path('question/', question, name='one_question'),
    path('check_answer/', check_answer, name='check_answer'),
    path('quantity/', quantity, name='quantity'),


]
