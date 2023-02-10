from fastapi import APIRouter

welcome = APIRouter()


@welcome.get("/", include_in_schema=False)
async def start_welcome():
    """Welcome to the python microservice template"""
    return "Welcome to the Python Template API. For more information, read the documentation in /docs or /redoc"
