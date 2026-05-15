from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuarios"])

@users_routes.post("/users")
async def criar_usuario():

    return JSONResponse(
        content={"Ola": "Mundo"},
        status_code=200
    )

