from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import AccountCreationForm
from django.contrib.auth import login


def custom_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:profile'))
    else:
        return login(request)


def register(request):
    user = request.user
    if user.is_authenticated:
        return redirect(reverse('accounts:profile'))

    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '회원가입 성공')

            return redirect(reverse('accounts:login'))
        else:
            messages.add_message(request, messages.INFO, '회원가입 실패')
    else:
        form = AccountCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})
