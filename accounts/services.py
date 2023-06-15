from django.contrib.auth import get_user_model

import logging

from accounts.interfaces import AbstractUserRepository
from accounts.dto import CustomUserDTO
from accounts.exeptions import UserAlreadyExistsError

User = get_user_model()
logger = logging.getLogger('accounts')


class CustomUserServices:

    """ Represents a domain/business logic relates to CustomUser model"""
    def __init__(self, repository: AbstractUserRepository):
        self.repository = repository

    def register_new_user(self, user_dto: CustomUserDTO) -> CustomUserDTO:

        """ Performs registration of new CustomUser object """

        email = user_dto.email
        username = user_dto.username
        password = user_dto.password

        if self.repository.get_user_by_email(email) or self.repository.get_user_by_username(username):
            raise UserAlreadyExistsError

        new_user = self.repository.create_user(user_dto)
        logger.info(f"New user created | Username: [{username}] | Email: [{email}]")
        return new_user
