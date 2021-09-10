# login/views.py
from django import forms
from django.core.handlers import exception
from django.shortcuts import render, redirect
from rest_framework import viewsets

from login import models
from login.forms import UserForm, RegisterForm
from login.models import User
from map.serializers import UserSerializer


def index(request):
    pass
    return render(request, 'templates/index.html')


def get(self, request, *args, **kwargs):
    if isinstance(request.user, User):
        return self.list(request, *args, **kwargs)
    else:
        raise exception.NotAcceptable


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check the content！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect('/index/')
                else:
                    message = "The password is incorrect！"
            except:
                message = "Username does not exist！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Please check the content！"
        if register_form.is_valid():  # get data
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "The two passwords entered are different！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'The user already exists!'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'This email address has already been registered!'
                    return render(request, 'register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def map(request):
    pass
    return render(request, 'map.html')


def logout(request):
    request.session.flush()

    if not request.session.get("is_login", None):
        return redirect('/login/')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
