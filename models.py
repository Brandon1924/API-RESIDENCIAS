from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Alumno(Base):
    __tablename__ = 'alumnos'
    numero_control = Column(String(8), primary_key=True)
    nombre = Column(String, nullable=False)
    semestre = Column(Integer, nullable=False)
    carrera = Column(String(3), nullable=False)
    empresa_alumno = relationship("EmpresaAlumno", back_populates="alumno")

class Empresa(Base):
    __tablename__ = 'empresas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    rfc = Column(String(13), nullable=False)
    telefono = Column(String(15), nullable=False)
    empresa_alumnos = relationship("EmpresaAlumno", back_populates="empresa")

class EmpresaAlumno(Base):
    __tablename__ = "empresa_alumno"
    id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(String, ForeignKey("alumnos.numero_control"))
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    alumno = relationship("Alumno")
    empresa = relationship("Empresa")
