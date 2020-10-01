from django.urls import path

from .import views

urlpatterns = [
    path('dataVisual/', views.dataVisual, name='dataVisual'),
]