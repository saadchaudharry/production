from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .form import LoginForm

# Create your views here.


def Login(request):
    form = LoginForm(request.POST or None)
    params = {
        "form": form
    }
    print("User Logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # context['form'] = LoginForm()
            return (redirect("Products:p-all"))
        else:
            # Return an 'Invalid login' error message
            print("error")
    return render(request,'auth/login.html',params)
