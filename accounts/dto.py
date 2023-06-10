from typing import NamedTuple


class UserDTO(NamedTuple):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
