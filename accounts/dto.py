from typing import NamedTuple


class CustomUserDTO(NamedTuple):

    """ User data object build to contain and transport User model data """

    username: str
    email: str
    password: str
    first_name: str = None
    last_name: str = None
