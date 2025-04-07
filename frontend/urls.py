# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('qr/', views.qr_code_view, name='qr-code'),
]
