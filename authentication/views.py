from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
# Create your views here.
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You are logged out!!! ")
        return redirect('login')


class LoginView(View):
    ''' This is the login view '''
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successfull')
            return redirect('emp-index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

class RegisterView(View):
    ''' This is register view '''
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user:
                messages.error(request, 'Username already exists. Try new one.')
                return redirect('register')
        except:
            data = User.objects.create_user(
             first_name=first_name,
             last_name=last_name, 
             email=email, 
             username=username, 
             password=password)
            messages.success(request, 'Account registered successfully.')
            send_mail(
                'Account creation | ERS', #subject
                'Your account has been created!! Welcome ' + data.username, #message
                'alxthakuri@gmail.com', #sender
                [data.email] #reciever
                )
            return redirect('login')
            


    def get(self, request):
        return render(request, 'authentication/register.html')

