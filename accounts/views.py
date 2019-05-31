from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import AccountCreationForm, LoginForm
from django.contrib.auth import login, authenticate


def custom_login(request):
    user = request.user
    if user.is_authenticated:
        return redirect(reverse('accounts:profile'))
    elif request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(
            username=form['username'].value(),
            password=form['password'].value(),
        )
        if user is not None:
            login(request, user)
            return redirect(reverse('accounts:profile'))
        else:
            messages.add_message(request, messages.INFO, "아이디나 비밀번호를 다시 생각해보세요")

    return render(request, 'accounts/login.html', {
        'user': user,
        'form': LoginForm(),
    })


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

    return render(request, 'accounts/register.html', {
        'user': user,
        'form': form,
    })


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})
