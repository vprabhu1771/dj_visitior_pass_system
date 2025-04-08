# urls.py
from django.urls import path
from frontend.views import home, qr_code_view, webcam_feed

urlpatterns = [
    path('', home, name='home'),
    path('qr/', qr_code_view, name='qr-code'),
    path('webcam/', webcam_feed, name='webcam-feed'),
]
