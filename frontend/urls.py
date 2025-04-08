# urls.py
from django.urls import path
from frontend.views import home, qr_code_view

urlpatterns = [
    path('', home, name='home'),
    path('qr/', qr_code_view, name='qr-code'),
]
