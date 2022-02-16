from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Cards
from .form import OrderForm, CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
    cards = Cards.objects.all()
    ctx = {'cards': cards}
    return render(request, 'homepage.html', ctx)


@login_required(login_url='login')
def app(request):
    cards = Cards.objects.filter(author=request.user)
    ctx = {'cards': cards}
    return render(request, 'cards.html', ctx)


def sign_up_view(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # log the user in
            return redirect('login')
    form = CreateUser()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('login')


def add_card(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('desc'):
            card = Cards()
            card.title = request.POST.get('title')
            card.desc = request.POST.get('desc')
            card.author = request.POST.get('author')
            card.save()
    return redirect('app')


def card(request):
    return render(request, 'add_card.html')
