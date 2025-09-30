# accounts/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class RegisterView(APIView):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user=user)
            return redirect('login')
        return render(request, 'accounts/register.html', {'errors': serializer.errors})


class LoginView(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successful', 'token': token.key})
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

class DashboardView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        return render(request, 'accounts/dashboard.html', {'token': token})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # This logs out the user
        return render(request, 'registration/logged_out.html')  # Custom template