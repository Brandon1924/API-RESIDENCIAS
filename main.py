from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, Alumno, Empresa, EmpresaAlumno
from database import engine, SessionLocal
from schemas import AlumnoCreate, Alumno as AlumnoResponse, EmpresaCreate, Empresa as EmpresaResponse, EmpresaAlumnoCreate, EmpresaAlumno as EmpresaAlumnoResponse

app = FastAPI()

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas para Alumno
@app.post("/alumnos/", response_model=AlumnoResponse)
def create_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    db_alumno = Alumno(**alumno.dict())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

@app.get("/alumnos/", response_model=list[AlumnoResponse])
def read_alumnos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    alumnos = db.query(Alumno).offset(skip).limit(limit).all()
    return alumnos

@app.get("/alumnos/{numero_control}", response_model=AlumnoResponse)
def read_alumno(numero_control: str, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.numero_control == numero_control).first()
    if alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@app.put("/alumnos/{numero_control}", response_model=AlumnoResponse)
def update_alumno(numero_control: str, alumno: AlumnoCreate, db: Session = Depends(get_db)):
    db_alumno = db.query(Alumno).filter(Alumno.numero_control == numero_control).first()
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    for key, value in alumno.dict().items():
        setattr(db_alumno, key, value)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

@app.delete("/alumnos/{numero_control}")
def delete_alumno(numero_control: str, db: Session = Depends(get_db)):
    db_alumno = db.query(Alumno).filter(Alumno.numero_control == numero_control).first()
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    db.delete(db_alumno)
    db.commit()
    return {"detail": "Alumno eliminado"}

# Rutas para Empresa
@app.post("/empresas/", response_model=EmpresaResponse)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/", response_model=list[EmpresaResponse])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    empresas = db.query(Empresa).offset(skip).limit(limit).all()
    return empresas

@app.get("/empresas/{empresa_id}", response_model=EmpresaResponse)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa

@app.put("/empresas/{empresa_id}", response_model=EmpresaResponse)
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    for key, value in empresa.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    db.delete(db_empresa)
    db.commit()
    return {"detail": "Empresa eliminada"}

# Rutas para Empresa-Alumno
@app.post("/empresa_alumno/", response_model=EmpresaAlumnoResponse)
def create_empresa_alumno(empresa_alumno: EmpresaAlumnoCreate, db: Session = Depends(get_db)):
    db_empresa_alumno = EmpresaAlumno(**empresa_alumno.dict())
    db.add(db_empresa_alumno)
    db.commit()
    db.refresh(db_empresa_alumno)
    return db_empresa_alumno
