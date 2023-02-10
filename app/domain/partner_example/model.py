from sqlalchemy import Boolean, Column, String

from app.domain.common.entity_model_base import EntityModelBase


class PartnerExample(EntityModelBase):
    __tablename__ = "partner_example"

    document = Column(String(14), unique=True, index=True)
    name = Column(String(128))
    active = Column(Boolean(), default=True)

    def __repr__(self):
        return f'<PartnerExample(id={self.id}, document="{self.document}", name="{self.name}", active={self.active})>'
