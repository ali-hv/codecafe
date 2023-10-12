from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm


def get_persian_errors(form):
    persian_errors = {'A user with that username already exists': 'این نام کاربری قبلا استفاده شده است',
                      'This password is too short': 'رمز عبور خیلی کوتاه است',
                      ' It must contain at least 8 characters': 'رمز عبور باید حداقل شامل 8 کاراکتر باشد',
                      'This password is too common': 'رمز عبور خیلی ساده است',
                      'The two password fields didn’t match': 'پسورد ها یکسان نیستند',
                      'This password is entirely numeric': 'رمز عبور تنها از اعداد تشکیل شده است. باید شامل اعداد و حروف باشد', }

    form_errors = list(form.errors.values())
    form_errors = [''.join(i) for i in form_errors]
    form_errors = ''.join(form_errors)
    form_errors = form_errors.split('.')
    form_errors = [i for i in form_errors if len(i) != 0]
    form_errors = [persian_errors.get(i, 'اطلاعات ورودی صحیح نیستند') for i in form_errors]

    return form_errors


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username_input = login_form.cleaned_data.get('username')
            password_input = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')
            else:
                login_form.add_error('password', 'نام کاربری یا رمز عبور صحیح نیستند')
    context = {'login_form': login_form}
    return render(request, 'registration/login.html', context)


def register_page(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home_page')
    else:
        form = UserRegisterForm()

    form_errors = get_persian_errors(form)
    context = {'register_form': form, 'register_form_errors': form_errors}
    return render(request, 'registration/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home:home_page')
