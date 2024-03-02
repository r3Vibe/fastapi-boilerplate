""" main api file """

from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """on startup we will initialize our database"""
    from app.database.db import get_db

    await get_db()
    yield


""" initialize app with openapi configurations """
app = FastAPI(
    title="Boilerplate",
    summary="FastApi boilerplate for all project",
    description="""
    FastApi boilerplate that will include basic structure and authentication
    """,
    version="0.0.5",
    servers=[
        {
            "url": "http://127.0.0.1:8000/api/v1",
            "description": "Local Server"
        }
    ],
    root_path="/api/v1",
    root_path_in_servers=False,
    lifespan=lifespan,
)

# cors policy
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount the static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# mount the templets folder
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root(request: Request):
    """set the root to show a html welcome page"""
    return templates.TemplateResponse(request=request, name="index.html")


# include all the other api endpoints
app.include_router(routes.router)
