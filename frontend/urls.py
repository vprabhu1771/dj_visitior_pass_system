# urls.py
from django.urls import path
from frontend.views import home, qr_code_view, webcam_feed, register, decode_qr_from_image, search, scan_qr

urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('/home', home, name='home'),

    # Search
    path('search', search, name='search'),

    # Scan QR
    path('scan_qr', scan_qr, name='scan_qr'),

    path('webcam/', webcam_feed, name='webcam-feed'),
    path('qr-code/', qr_code_view, name='qr-code'),
    path('decode-qr/', decode_qr_from_image, name='decode-qr'),

    path('webcam/', webcam_feed, name='webcam-feed'),
    path('register', register, name='register')
]
