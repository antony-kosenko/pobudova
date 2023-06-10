from django.contrib import messages
from django.contrib.auth import login, get_user_model, authenticate, logout

import logging

from accounts.forms import CreateUserForm

User = get_user_model()
logger = logging.getLogger('accounts')


def authenticate_user(request) -> User:

    """ Authenticates user by given credentials"""

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    return user


def login_user(request, user: User) -> User:

    """ Logs user in using default django 'login' function and sets status of user to 'online'"""

    login(request, user)
    user.online = True
    user.save()
    logger.info(f"UserID: [{user.id}] logged in. ONLINE")

    return user


def logout_user(request):

    """ Logs out a current uses and sets his status to 'offline'. """

    user = request.user
    logout(request)
    logger.info(f"UserID{user.id} has logged out")
    user.online = False
    user.save(update_fields=['online'])


def register_new_user(request, new_user: CreateUserForm):

    """ Handles a registration process with validation and returns a new user object just registered """

    if new_user.is_valid():
        new_user.save()
        user_name = new_user.cleaned_data.get('username')
        logger.info(f"New user registered ID: [{new_user.auto_id}]")
        messages.success(request, f'User {user_name} successfully created')

        return new_user
