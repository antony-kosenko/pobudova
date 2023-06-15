from typing import List

from django.contrib.auth import get_user_model

from accounts.dto import CustomUserDTO
from accounts.interfaces import AbstractUserRepository


CustomUser = get_user_model()


class CustomUserRepository(AbstractUserRepository):

    """ User model repository. Represents an abstract layer to interact with DB.
     Allows to interact with the model utilizing third party ORMs and adaptors.
     Inherits from ABC metaclass (blueprint).
     """

    def create_user(self, user_data: CustomUserDTO) -> CustomUserDTO:

        """ Creates a new CustomUser object with DTO object provided as argument """

        user = CustomUser.objects.create_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            is_active=True
        )

        return self._user_object_to_dto(user)

    def get_all_users(self) -> List[CustomUserDTO]:

        """ Fetches all CustomUser objects rom DB and returns them as List of DTO objects. """

        all_users = CustomUser.objects.all()
        return self._user_queryset_to_dto(all_users)

    def get_user_by_id(self, user_id: str) -> CustomUserDTO | None:
        user = CustomUser.objects.filter(id=user_id).first()
        return self._user_object_to_dto(user) if user else None

    def get_user_by_email(self, user_email: str) -> CustomUserDTO | None:
        user = CustomUser.objects.filter(email=user_email).first()
        return self._user_object_to_dto(user) if user else None

    def get_user_by_username(self, username: str) -> CustomUserDTO | None:
        user = CustomUser.objects.filter(username=username).first()
        return self._user_object_to_dto(user) if user else None

    def update_user_password(self, user_id: str, new_password: str) -> None:
        user = CustomUser.objects.get(id=user_id)
        user.set_password(new_password)
        user.save(update_fields=["password"])

    def delete_user(self, user_id: str) -> None:
        user = CustomUser.objects.get(id=user_id)
        user.delete()

    def deactivate_user(self, user_id: str) -> None:
        user = CustomUser.objects.get(id=user_id)
        user.is_active = False

    @staticmethod
    def _user_object_to_dto(user: CustomUser) -> CustomUserDTO:
        """ Translates a CustomUser object to UserDTO object """
        return CustomUserDTO(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password
        )

    def _user_queryset_to_dto(self, user_queryset) -> List[CustomUserDTO]:
        # TODO 'user_queryset' type hint?
        """ Translates a queryset of CustomUser objects to list of CustomUser DTO """

        list_of_users_dto = [self._user_object_to_dto(user) for user in user_queryset]

        return list_of_users_dto

