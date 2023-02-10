from typing import Optional

from pydantic import BaseModel, validator
from validate_docbr import CNPJ, CPF

from app.domain.partner_example.exceptions import InvalidDocumentException


class PartnerCreate(BaseModel):
    name: str
    document: str
    active: bool

    @validator("document")
    def validate_document(cls, value):
        """Validate the document
        :param: value: the document to validate

        :return: the document
        :raises: InvalidDocumentException
        """
        if not CPF().validate(value) and not CNPJ().validate(value):
            raise InvalidDocumentException()

        value = "".join(v for v in value if v.isalnum())

        return value


class PartnerUpdate(PartnerCreate):
    id: int


class Partner(PartnerUpdate):
    class Config:
        orm_mode = True


class Email(BaseModel):
    sender_email: Optional[str] = ""
    message: str

    @validator("sender_email")
    def validate_sender_email(cls, value):
        """Validate the sender_email
        :param: value: the sender_email to validate

        :return: the sender_email or add some fake email
        """
        return value or "fakeemail@.com.br"
