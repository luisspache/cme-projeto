from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, auth

app = FastAPI()

# Conecta com o banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Permitir acesso do frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode ajustar depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas de autenticação e materiais
app.include_router(auth.router)
