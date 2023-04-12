from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

import logging

from accounts.forms import CreateUserForm


logger = logging.getLogger('accounts')


def register_view(request):
    """ Registration of a new User.
     Contains a registration form handles a communication with DB to create a new User object"""
    form = CreateUserForm
    if request.method == 'POST':
        new_user = CreateUserForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            user_name = new_user.cleaned_data.get('username')
            logger.info(f"New user registered ID: [{new_user.auto_id}]")
            messages.success(request, f'User {user_name} successfully created')
            return redirect('accounts:login')

    context = {
        "user_creation_form": form
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    """ Login page.
     Contains a login form for authentication and authorization a User.
     Allows a User to enter a Home page if logged in successfully"""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validating a data as per given credentials
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Login or/and Password are not matching with actual user")
            return render(request, 'accounts/login.html')
        else:
            # Login user. Change his network status to Online
            login(request, user)
            logger.info(f"UserID: [{user.id}] logged in. ONLINE")
            user.online = True
            user.save()
            return redirect(reverse('core:home'), user=user)

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    """ Logout function.
    Closes a User session."""

    user = request.user
    logout(request)
    logger.info(f"UserID{user.id} has logged out")
    user.online = False
    user.save()
    return redirect(reverse('core:start'))
