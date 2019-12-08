from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from accounts.form import Extendusermodel

def home(request):
    # name=request.session.get('first_name',"unknown")
    # print(name)
    return redirect('Products:p-all')

def contact(request):
    a=Extendusermodel(request.POST)
    return render(request ,'contact.html',{'form':a})

def regester(request):
    if request.method == 'POST':
        f = Extendusermodel(request.POST)
        if f.is_valid():
            is_staff = request.POST.get(True)

            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('Login')
    else:
        f = Extendusermodel()

    return render(request, 'regester.html', {'form':f})

def loog(request):
    # if request.method == 'POST':
    # username = ("username")
    # password = ("password")
    # f = authenticate(request.POST,username,password)
    # f.save()
    #     # messages.success(request, 'Account created successfully')
    #         return redirect('Products:p-all')
    # else:
    #     f = AuthenticationForm()

    return render(request, 'regester.html')
# def Login(request):
#     form = LoginForm(request.POST or None)
#     params = {
#         "form": form
#     }
#     print("User Logged in")
#     print(request.user.is_authenticated)
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         print(request.user.is_authenticated)
#         if user is not None:
#             print(request.user.is_authenticated)
#             login(request, user)
#             # context['form'] = LoginForm()
#             return (redirect("/login"))
#         else:
#             # Return an 'Invalid login' error message
#             print("error")
#     return render(request,'auth/login.html',params)



