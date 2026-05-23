from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdf_search, name='pdf_search'),
]
