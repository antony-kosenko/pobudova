from abc import ABC, abstractmethod
from typing import List

from accounts.dto import CustomUserDTO


class AbstractUserRepository(ABC):

    @abstractmethod
    def create_user(self, user_data: CustomUserDTO) -> CustomUserDTO:
        pass

    @abstractmethod
    def get_all_users(self) -> List[CustomUserDTO]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> CustomUserDTO | None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> CustomUserDTO | None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> CustomUserDTO | None:
        pass

    @abstractmethod
    def update_user_password(self, user_id: str, new_password: str) -> None:
        pass

    @abstractmethod
    def delete_user(self, user_id: str) -> None:
        pass

    @abstractmethod
    def deactivate_user(self, user_id: str) -> None:
        pass
