from django.core.exceptions import ValidationError


class UserAlreadyExistsError(ValidationError):
    def __init__(self, message="User with this email or username already exists", *args, **kwargs):
        super().__init__(message, *args, **kwargs)