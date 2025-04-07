# views.py
from django.http import HttpResponse, Http404
from .utils import generate_qr_code
from backend.models import CustomUser


def qr_code_view(request):
    user_id = request.GET.get('id')  # expects ?id=1
    if not user_id:
        return HttpResponse("User ID not provided", status=400)

    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404("User not found")

    # Customize QR data as needed
    data = f"ID: {user.id}\nName: {user.first_name} {user.last_name}\nEmail: {user.email}\nPhone: {user.phone_no}"

    qr_image = generate_qr_code(data)
    return HttpResponse(qr_image, content_type='image/png')
