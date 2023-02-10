from starlette import status

from app.domain.common.exception_base import APIException


class InvalidDocumentException(APIException):
    def __init__(self):
        detail = "Invalid CPF/CNPJ"
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail, severity=20)


class UnauthorizedException(APIException):
    def __init__(self):
        detail = "Unauthorized user for feature-flag"
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, severity=20)
