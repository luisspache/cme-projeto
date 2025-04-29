from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

# Tipos de usuário
class RoleEnum(str, enum.Enum):
    tecnico = "tecnico"
    enfermagem = "enfermagem"
    administrativo = "administrativo"

# Tabela de usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum))

# Tabela de materiais
class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    expiration_date = Column(Date)
    serial = Column(String, unique=True)

# Tabela de rastreabilidade
class MaterialTracking(Base):
    __tablename__ = "material_tracking"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    step = Column(String)  # Recebimento, Lavagem, Esterilização, Distribuição
    failure = Column(String, nullable=True)

    material = relationship("Material")
