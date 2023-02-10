import pytest

from app.domain.common.exception_base import NotFoundException, UniqueException
from app.domain.partner_example.repository import Repository
from app.domain.partner_example.schemas import PartnerCreate
from app.domain.partner_example.service import Service


@pytest.fixture
@pytest.mark.usefixtures("session_db")
@pytest.mark.usefixtures("metadata_create_all")
def repository(metadata_create_all, session_db):
    return Repository(session=session_db)


@pytest.fixture
def service(repository):
    return Service(repository=repository)


@pytest.fixture
def partner_schema():
    return PartnerCreate(name="Test Unit Partner", document="674.194.620-97", active=True)


@pytest.fixture()
@pytest.mark.asyncio
async def create_partner(service, partner_schema):
    try:
        return await service.get_partner_by_document(partner_schema.document)
    except NotFoundException:
        return await service.create_partner(partner_schema)


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
async def test_get_partner_by_id_raise_not_found_exception(service, cap_logger):
    partner_id = 1

    with pytest.raises(NotFoundException), cap_logger.at_level(20):
        await service.get_partner_by_id(partner_id)

        assert "[-] partner_example not found - Status=[404]" in cap_logger.records[0].message
        assert "INFO" == cap_logger.records[0].levelname


@pytest.mark.asyncio
async def test_get_partner_by_id_return_partner(service, create_partner):
    new_partner = await create_partner
    partner = await service.get_partner_by_id(new_partner.id)

    assert partner.name == new_partner.name
    assert partner.document == new_partner.document
    assert partner.active == new_partner.active


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
async def test_get_partner_by_document_raise_not_found_exception(service, cap_logger):
    document = "674.194.620-97"

    with pytest.raises(NotFoundException), cap_logger.at_level(20):
        await service.get_partner_by_document(document)

        assert "[-] partner_example not found - Status=[404]" in cap_logger.records[0].message
        assert "INFO" == cap_logger.records[0].levelname


@pytest.mark.asyncio
async def test_get_partner_by_document_return_partner(service, create_partner):
    new_partner = await create_partner
    partner = await service.get_partner_by_document(new_partner.document)

    assert partner.name == new_partner.name
    assert partner.document == new_partner.document
    assert partner.active == new_partner.active


@pytest.mark.asyncio
async def test_get_all_partner_return_partners(service, create_partner):
    new_partner = await create_partner
    partners = await service.get_all_partner()

    assert len(partners) > 0
    assert partners[0].name == new_partner.name
    assert partners[0].document == new_partner.document
    assert partners[0].active == new_partner.active


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
async def test_create_partner_raise_unique_exception(service, create_partner, partner_schema, cap_logger):
    new_partner = await create_partner

    with pytest.raises(UniqueException), cap_logger.at_level(30):
        await service.create_partner(new_partner)

        assert "[-] Unique constraint - the value already exists in the database" in cap_logger.records[0].message
        assert "WARNING" == cap_logger.records[0].levelname


@pytest.mark.asyncio
async def test_create_partner_return_partner(service):
    partner_name = "Partner Test Unit"
    partner_document = "916.638.390-00"
    partner = await service.create_partner(PartnerCreate(name=partner_name, document=partner_document, active=True))

    assert partner.name == partner_name
    assert partner.document == "91663839000"
    assert partner.active is True
