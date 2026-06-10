from fastapi import FastAPI
from app.resources.health_resource import router as health_router

def create_app() -> FastAPI:
    
    app = FastAPI(title="Gallatin Screen")
    
    # Include routers below, exception handlers below
    app.include_router(health_router)

    return app

app = create_app()