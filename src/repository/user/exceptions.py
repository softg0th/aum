class UserError(Exception):
    pass


class UserCreationError(UserError):
    pass


class UserCheckError(UserError):
    pass


class UserAlreadyExistsError(UserCreationError):
    pass


class UserNotFoundError(UserCheckError):
    pass


class UserPasswordIncorrectError(UserCheckError):
    pass
