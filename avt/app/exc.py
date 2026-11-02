class AppError(Exception):
    #корень ошибок.
    status_code = 500
    default_message = "Внутренняя ошибка"

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)


#ошибка на стороне клиента (4xx)

class BadRequestError(AppError):
    status_code = 400
    default_message = "Некорректный запрос"


class AuthenticationError(AppError):
    status_code = 401
    default_message = "Требуется авторизация"


class PermissionDeniedError(AppError):
    status_code = 403
    default_message = "Недостаточно прав"


class NotFoundError(AppError):
    status_code = 404
    default_message = "Не найдено"


class ConflictError(AppError):
    status_code = 409
    default_message = "Конфликт данных"


class TooManyRequestsError(AppError):
    status_code = 429
    default_message = "Слишком много запросов"


#проблема на стороне сервера (5xx)

class ServiceUnavailableError(AppError):
    status_code = 503
    default_message = "Сервис временно недоступен"


# Конкретные ошибки: пользователи и вход

class InvalidCredentials(AuthenticationError):
    default_message = "Неверный email или пароль"


class NotAuthenticated(AuthenticationError):
    default_message = "Необходимо войти в систему"


class EmailAlreadyRegistered(ConflictError):
    default_message = "Этот email уже зарегистрирован"


class UserNotFound(NotFoundError):
    default_message = "Пользователь не найден"


class WeakPassword(BadRequestError):
    default_message = "Пароль слишком простой"