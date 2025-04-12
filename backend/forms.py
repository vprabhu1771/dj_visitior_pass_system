from backend.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    class Meta:
        model = CustomUser
        # fields = ('email',)
        # fields = '__all__'
        fields = ('email', 'first_name', 'last_name', 'gender', 'dob', 'phone_no', )

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))


    class Meta:
        model = CustomUser
        fields = ('email',)