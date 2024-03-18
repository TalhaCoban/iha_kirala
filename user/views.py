from django.shortcuts import render, redirect
from user.forms import RegisterFrom, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):

    if request.method == "POST":
        form = RegisterFrom(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()

            login(request, newUser)

            messages.info(request, "başarıyla kayıt oldunuz")

            return redirect("index")

    else:
        form = RegisterFrom()
        context = {
            "form" : form
        }
        return render(request,"register.html", context)


def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request, "Kullanıcı Bulunamadı")
                form = LoginForm()
                context = {
                    "form" : form
                }
                return render(request, "login.html", context)
            
            else:
                messages.success(request,"Başarıyla Giriş Yaptınız")
                login(request, user)
                return redirect("index")
            
    else:
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request,"login.html", context)



def logoutUser(request):
    logout(request)
    messages.info(request,"Çıkış Yaptınız")
    return redirect("index")