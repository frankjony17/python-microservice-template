from fastapi import FastAPI

from app.internal.config import PROJECT_CONTACT_API, PROJECT_DESCRIPTION_API, PROJECT_VERSION_API, set_up_logger
from app.routers import healthcheck, partner, welcome

__version__ = PROJECT_VERSION_API


def create_app() -> FastAPI:
    """Instantiates and configures the FastAPI app.
    Includes all routers and middleware

    :returns: FastAPI: The configured and ready to use FastAPI application
    """
    # Set custom logger configurations (loguru)
    set_up_logger()

    # Create web framework app
    app = FastAPI(
        title="Python Microservice Template",
        description=PROJECT_DESCRIPTION_API,
        version=PROJECT_VERSION_API,
        contact=PROJECT_CONTACT_API,
    )
    app.include_router(router=welcome)
    app.include_router(partner.router, prefix="/partner", tags=["Partner"])
    app.include_router(healthcheck.router, tags=["Health"])

    return app
