from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("trainee_list")  # Adjust this redirect as needed
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "register.html",)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")  
    return render(request, "logout.html")
