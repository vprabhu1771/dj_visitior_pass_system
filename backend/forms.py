from backend.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = ('email',)
        # fields = '__all__'
        fields = ('email', 'first_name', 'last_name', 'gender', 'dob', 'phone_no', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)