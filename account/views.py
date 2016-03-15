__author__ = 'ali-pc'
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm, ProfileForm


def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    next_url = request.GET.get('next', 'funeral:home')
    form = LoginForm(request.POST or None, auto_id=False)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect(next_url)
                else:
                    error = 'تم ايقاف هذا الحساب! الرجاء التواصل مع الادارة'
            else:
                error = 'اسم المستخدم او كلمة المرور غير صحيحة!'

    return render(request, 'account/login.html', {'form': form, 'error': error})


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated(): return redirect('funeral:home')
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password2'))
            auth.login(request, user)
            return redirect('funeral:home')
        else:
            context['form'] = form
            return render(request, 'account/register.html', context)
    form = RegisterForm()
    context['form'] = form
    return render(request, 'account/register.html', context)


@login_required()
def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['password1'] and form.cleaned_data['password2']:
                user.set_password(form.cleaned_data['password2'])
            user.save()

        context = {'title': 'تعديل البيانات', 'req_user': request.user, 'form': form}
        return render(request, 'account/profile.html', context)

    form = ProfileForm(instance=user)
    context = {'title': 'تعديل البيانات', 'req_user': request.user, 'form': form}
    return render(request, 'account/profile.html', context)
