from dependency_injector import containers, providers

from accounts.repositories import CustomUserRepository
from accounts.services import CustomUserServices


class UserServiceRepositoryContainer(containers.DeclarativeContainer):

    repository = providers.Singleton(CustomUserRepository)
    services = providers.Factory(
        CustomUserServices,
        repository=repository
    )
