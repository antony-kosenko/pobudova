from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import CreateUserForm
from accounts.services import login_user, authenticate_user, logout_user, register_new_user


def register_view(request):

    """ Registration of a new User.
     Contains a registration form handles a communication with DB to create a new User object"""

    form = CreateUserForm

    if request.method == 'POST':
        # Performs a creation of new user.
        new_user = CreateUserForm(request.POST)
        register_new_user(request, new_user=new_user)
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
        # Validating a data as per given credentials. Takes 'username' and 'password' from a request.
        user = authenticate_user(request)

        if user is None:
            messages.error(request, "Login or/and Password are not matching with actual user")
            return render(request, 'accounts/login.html')

        else:
            # Login user
            login_user(request, user=user)
            return redirect(reverse('core:home'), user=user)

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):

    """ Logout view. Closes a User session."""

    logout_user(request)
    return redirect(reverse('core:start'))
