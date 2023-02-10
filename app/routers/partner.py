from fastapi import APIRouter, BackgroundTasks, Depends

from app.dependencies import access_validation, get_repository
from app.domain.common.schema_base import DefaultResponse
from app.domain.partner_example import tasks
from app.domain.partner_example.repository import Repository
from app.domain.partner_example.schemas import Email, Partner, PartnerCreate, PartnerUpdate
from app.domain.partner_example.service import Service
from app.internal.utils import latency

router = APIRouter(dependencies=[Depends(access_validation)])


@router.get("/", summary="Get partners", response_model=list[Partner], status_code=200)
@latency
async def read_partners(
    skip: int = 0, limit: int = 100, repository: Repository = Depends(get_repository(repo_type=Repository))
):
    """Get partners from database
    * **param**: skip: Skip page in list of Partners
    * **param**: limit: Limit items in list of Partners
    * **param**: repository: Session of sql database

    **return**: list[Partner]
    """
    return await Service(repository=repository).get_all_partner(skip=skip, limit=limit)


@router.get("/document/{document}", summary="Get partner by document", response_model=Partner, status_code=200)
@latency
async def read_partner_by_document(
    document: str, repository: Repository = Depends(get_repository(repo_type=Repository))
):
    """Get partner by document
    * **param**: document: Document of the Partner
    * **param**: session_db: Session of sql database

    **return**: Partner
    """
    return await Service(repository=repository).get_partner_by_document(document)


@router.get("/{partner_id}", summary="Get partner by id", response_model=Partner, status_code=200)
@latency
async def read_partner_by_id(partner_id: int, repository: Repository = Depends(get_repository(repo_type=Repository))):
    """Get Partner by id
    * **param**: partner_id: ID to find the Partner
    * **param**: session_db: Session of sql database

    **return**: Partner
    """
    return await Service(repository=repository).get_partner_by_id(partner_id)


@router.post("/", summary="Create partner", response_model=DefaultResponse, status_code=201)
@latency
async def create_partner(data: PartnerCreate, repository: Repository = Depends(get_repository(repo_type=Repository))):
    """Create partner
    * **param**: data: PartnerCreate data payload
    * **param**: session_db: Session of sql database

    **return**: DefaultResponse
    """
    partner = await Service(repository=repository).create_partner(data)

    return DefaultResponse(data=[{"Partner": partner}])


@router.put("/", summary="Update partner", response_model=DefaultResponse, status_code=200)
@latency
async def update_partner(data: PartnerUpdate, repository: Repository = Depends(get_repository(repo_type=Repository))):
    """Update Partner
    * **param**: data: PartnerUpdate data payload
    * **param**: session_db: Session of sql database

    **return**: DefaultResponse
    """
    partner = await Service(repository=repository).update_partner(data)

    return DefaultResponse(data=[{"Partner": partner}])


@router.delete("/{partner_id}", summary="Delete partner", status_code=204)
@latency
async def delete_partner(partner_id: int, repository: Repository = Depends(get_repository(repo_type=Repository))):
    """Delete partner
    * **param**: partner_id: Partner id
    * **param**: session_db: Session of sql database

    **return**: None
    """
    await Service(repository=repository).delete_partner(partner_id)


@router.post(
    "/send_email", summary="Send fake email - Use BackgroundTasks", response_model=DefaultResponse, status_code=202
)
@latency
async def email(data: Email, background_tasks: BackgroundTasks):
    """You can define background tasks to be run after returning a response.

       BackgroundTasks runs in the same event loop that serves your app's requests.

       https://fastapi.tiangolo.com/tutorial/background-tasks/

    * **param**: data: Email data payload
    * **param**: background_tasks: background tasks object

    **return**: DefaultResponse
    """
    background_tasks.add_task(tasks.send_email_background, sender_email=data.sender_email, message=data.message)

    return DefaultResponse(data=[{"message": "Email sent in the background"}])
