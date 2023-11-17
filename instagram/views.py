from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import profileForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index (request):
    return render(request, "instagram/index.html")


def sign_up(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('instagram:index')) 
        return render(request, "instagram/instagram_signup.html")
    elif request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return HttpResponseRedirect(reverse('instagram:login')) 

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('instagram:index')) 
        return render(request, "instagram/instagram_login.html")
    elif request.method == "POST":
        username = request.POST.get('username') # POST["username"]
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('instagram:index')) 
        else:
            return render(request, "instagram/instagram_login.html", {"login_message": "Username/password is incorrect"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('instagram:login')) 


def index_view (request):
    profile = profileForm()
    return render(request, 'instagram/index.html', { 'form': profile })

def form_submit(request):
    form = profileForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'instagram/thank-you.html', {})
    else:
        return render(request, 'instagram/index.html', {'form': form})