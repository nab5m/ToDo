from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone', 'birth_date']
