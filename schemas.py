from pydantic import BaseModel, Field

class AlumnoBase(BaseModel):
    nombre: str
    semestre: int
    carrera: str

class AlumnoCreate(AlumnoBase):
    numero_control: str = Field(..., pattern=r'^\d{8}$')  # 8 dígitos

class Alumno(AlumnoBase):
    numero_control: str

    class Config:
        orm_mode = True  # Esto permite usar el modelo de SQLAlchemy

class EmpresaBase(BaseModel):
    nombre: str
    direccion: str
    rfc: str
    telefono: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class Config:
        orm_mode = True

class EmpresaAlumnoBase(BaseModel):
    alumno_id: str
    empresa_id: int

class EmpresaAlumnoCreate(EmpresaAlumnoBase):
    pass

class EmpresaAlumno(EmpresaAlumnoBase):
    id: int

    class Config:
        orm_mode = True  # Esto permite usar el modelo de SQLAlchemy
