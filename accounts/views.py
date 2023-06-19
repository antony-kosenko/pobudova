from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import CreateUserForm
from accounts.dto import CustomUserDTO
from accounts.containers import UserServiceRepositoryContainer


def register_view(request):

    """ Registration of a new User """
    # Initializing a container responsible for dependency injection between CustomUser services and repository
    container = UserServiceRepositoryContainer()
    service = container.services()

    registration_form = CreateUserForm

    if request.method == 'POST':
        registration_form = CreateUserForm(request.POST)
        # Takes a data passed from a POST request (form), checks for validity and saves data as a new User object
        if registration_form.is_valid():

            # fetching form's data
            username = registration_form.cleaned_data["username"]
            email = registration_form.cleaned_data["email"]
            password = registration_form.cleaned_data["password1"]

            # bundling form's data to DTO
            new_user_dto = CustomUserDTO(username=username, email=email, password=password)
            service.register_new_user(new_user_dto)
            return redirect('accounts:login')

    context = {
        "user_creation_form": registration_form
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):

    """ Login page.
     Contains a login form for authentication and authorization a User.
     Allows a User to enter a Home page if logged in successfully"""

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validating a data as per given credentials. Takes 'username' and 'password' from a request.
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Login or/and Password are not matching with actual user")
            return render(request, 'accounts/login.html')

        else:
            # Login user
            login(request, user)
            return redirect(reverse('core:home'), user=user)

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):

    """ Logout view. Closes a User session."""

    logout(request)
    return redirect(reverse('core:start'))
