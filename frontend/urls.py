# urls.py
from django.urls import path
from frontend.views import home, qr_code_view, webcam_feed, register, decode_qr_from_image

urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('/home', home, name='home'),

    path('webcam/', webcam_feed, name='webcam-feed'),
    path('qr-code/', qr_code_view, name='qr-code'),
    path('decode-qr/', decode_qr_from_image, name='decode-qr'),

    path('webcam/', webcam_feed, name='webcam-feed'),
    path('register', register, name='register')
]
