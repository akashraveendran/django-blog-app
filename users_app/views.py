from django.shortcuts import render, redirect

from users_app.forms import UserAddForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_page(request):

    return render(request, "home.html")


def signin(request):

    return render(request, "signin.html")


def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect("Signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect("Signup")
            else:
                new_user = form.save()
                new_user.save()
                messages.info(request, "User Created")
                return redirect("signin")
        else:
            print("Hai")
            messages.info(
                request, "Validation Error please provide a strong password")

    return render(request, "signup.html", {"form": form})
