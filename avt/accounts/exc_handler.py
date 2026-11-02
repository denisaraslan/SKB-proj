from rest_framework.response import Response
from rest_framework.views import exception_handler

from app.exc import AppError


def app_exception_handler(exc, context):
    if isinstance(exc, AppError):
        return Response({"detail": exc.message}, status=exc.status_code)
    # остальное (ошибки валидации DRF, 403 от прав и т.д.) обрабатывает сам DRF
    return exception_handler(exc, context)