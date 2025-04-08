from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from backend.forms import CustomUserCreationForm
from .utils import generate_qr_code
from backend.models import CustomUser

import cv2
from django.http import StreamingHttpResponse

def gen_frames():
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # flip camera
            frame = cv2.flip(frame, 1)
            # Convert frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def webcam_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


def home(request):
    user = None
    query = request.GET.get('phone_no')
    if query:
        try:
            user = CustomUser.objects.get(phone_no=query)
        except CustomUser.DoesNotExist:
            user = None
    return render(request, "frontend/home.html", {"user": user})


def qr_code_view(request):
    user_id = request.GET.get('id')
    if not user_id:
        return HttpResponse("User ID not provided", status=400)
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404("User not found")

    data = f"ID: {user.id}\nName: {user.first_name} {user.last_name}\nEmail: {user.email}\nPhone: {user.phone_no}"

    qr_image = generate_qr_code(data)
    return HttpResponse(qr_image, content_type='image/png')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('home')  # or any success URL
            messages.success(request, "User registered successfully!")
            return redirect('register')  # 👈 redirect back to the register page
    else:
        form = CustomUserCreationForm()

    return render(request, "frontend/register.html", {'form': form})
