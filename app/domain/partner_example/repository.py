from app.domain.common.repository_base import RepositoryBase
from app.domain.partner_example.model import PartnerExample


# @dataclass
class Repository(RepositoryBase):
    def __init__(self, session):
        super().__init__(session)
        self.entity_model = PartnerExample

    async def find_partner_by_document(self, document: str) -> PartnerExample:
        """Find partner by document
        :param document: The document of the Partner

        :return: PartnerExample
        """
        return self.query().filter_by(document=document).first()
