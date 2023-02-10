from dataclasses import dataclass, field
from typing import Any, List, Optional, Type

from app.domain.common.service_base import ServiceBase, try_query_except
from app.domain.partner_example.model import PartnerExample
from app.domain.partner_example.repository import Repository
from app.domain.partner_example.schemas import PartnerCreate, PartnerUpdate


@dataclass
class Service(ServiceBase):
    repository: Repository
    sender_email: str = field(init=False)

    @try_query_except
    async def get_partner_by_id(self, partner_id: int) -> Optional[Type[PartnerExample]]:
        """Find partner for the given id
        :param partner_id: partner id

        :return: PartnerExample
        :raises NotFoundException or SQLAlchemyException
        """
        return await self.repository.get_by_id(partner_id)

    @try_query_except
    async def get_partner_by_document(self, document: str) -> PartnerExample:
        """Find partner for the given document
        :param document: document to find the partner

        :return: Partner
        :raises NotFoundException or SQLAlchemyError
        """
        partner = await self.repository.find_partner_by_document(document)

        return self.query_result(result=partner)

    @try_query_except
    async def get_all_partner(self, skip: int = 0, limit: int = 100) -> List[tuple[Any]]:
        """Find partner for the given document
        :param skip:
        :param limit:

        :return: List[PartnerExample]
        :raises NotFoundException or SQLAlchemyError
        """
        partners = await self.repository.get_all(skip, limit)

        return self.query_result(result=partners)

    @try_query_except
    async def create_partner(self, schema: PartnerCreate) -> PartnerExample:
        """Create partner
        :param schema: PartnerCreate

        :return: new PartnerExample
        :raises UniqueException or SQLAlchemyException
        """
        partner = PartnerExample(document=schema.document, name=schema.name, active=schema.active)

        return await self.repository.save(partner)

    @try_query_except
    async def update_partner(self, schema: PartnerUpdate) -> tuple[Any]:
        """Update partner
        :param schema: PartnerUpdate

        :return: PartnerExample updated
        :raises UniqueException or SQLAlchemyException
        """
        values = schema.dict()
        del values["id"]

        partner = await self.repository.update(schema.id, values)

        return self.query_result(result=partner)

    @try_query_except
    async def delete_partner(self, partner_id: int) -> None:
        """Delete a partner
        :param partner_id: partner id

        :return: None
        :raises SQLAlchemyException
        """
        partner = await self.get_partner_by_id(partner_id)
        await self.repository.delete(partner)
