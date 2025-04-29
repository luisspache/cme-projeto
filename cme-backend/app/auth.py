from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, database
from datetime import date
import random
import string

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependência para obter a sessão do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utilitários de senha
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# --------------------------
# USUÁRIOS
# --------------------------

@router.post("/register/")
def register_user(username: str, password: str, role: models.RoleEnum, db: Session = Depends(get_db)):
    hashed = hash_password(password)
    user = models.User(username=username, hashed_password=hashed, role=role)
    db.add(user)
    db.commit()
    return {"message": "Usuário criado com sucesso."}

@router.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "Login bem-sucedido", "user": {"username": user.username, "role": user.role}}

# --------------------------
# MATERIAIS
# --------------------------

@router.post("/materials/")
def create_material(name: str, type: str, expiration_date: date, db: Session = Depends(get_db)):
    serial = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    material = models.Material(name=name, type=type, expiration_date=expiration_date, serial=serial)
    db.add(material)
    db.commit()
    db.refresh(material)
    return material

@router.get("/materials/")
def list_materials(db: Session = Depends(get_db)):
    return db.query(models.Material).all()

# --------------------------
# RASTREAMENTO
# --------------------------

@router.post("/track/")
def track_material(serial: str, step: str, failure: str = None, db: Session = Depends(get_db)):
    material = db.query(models.Material).filter(models.Material.serial == serial).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    track = models.MaterialTracking(material_id=material.id, step=step, failure=failure)
    db.add(track)
    db.commit()
    return {"message": f"Etapa '{step}' registrada para o material {serial}."}

@router.get("/tracking/{serial}")
def get_tracking(serial: str, db: Session = Depends(get_db)):
    material = db.query(models.Material).filter(models.Material.serial == serial).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    tracking = db.query(models.MaterialTracking).filter(models.MaterialTracking.material_id == material.id).all()
    return tracking
    
    from fastapi.responses import StreamingResponse


import io
import openpyxl

@router.get("/export/{serial}")
def export_tracking(serial: str, db: Session = Depends(get_db)):
    material = db.query(models.Material).filter(models.Material.serial == serial).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    tracking = db.query(models.MaterialTracking).filter(models.MaterialTracking.material_id == material.id).all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Rastreabilidade"

    # Cabeçalho
    ws.append(["Etapa", "Falha"])

    # Dados
    for etapa in tracking:
        ws.append([etapa.step, etapa.failure or ""])

    # Salvar para um buffer
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                              headers={"Content-Disposition": f"attachment; filename=rastreabilidade_{serial}.xlsx"})

