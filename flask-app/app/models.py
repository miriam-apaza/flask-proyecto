from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
import datetime

class Area(Model):
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False) # Ejemplo: Tecnología, Idiomas
    
    # Relación uno a muchos con Curso utilizando back_populates
    cursos = relationship("Curso", back_populates="area")

    def __repr__(self):
        return self.nombre

class Curso(Model):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    costo = Column(Float, nullable=False)
    area_id = Column(Integer, ForeignKey('area.id'), nullable=False)
    
    # Relaciones bidireccionales
    area = relationship("Area", back_populates="cursos")
    inscripciones = relationship("Inscripcion", back_populates="curso")

    def __repr__(self):
        return self.nombre

class Estudiante(Model):
    __tablename__ = 'estudiante'
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(150), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    
    # Relación uno a muchos con Inscripcion
    inscripciones = relationship("Inscripcion", back_populates="estudiante")

    def __repr__(self):
        return self.nombre_completo

class Inscripcion(Model):
    __tablename__ = 'inscripcion'
    id = Column(Integer, primary_key=True)
    fecha_inscripcion = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    curso_id = Column(Integer, ForeignKey('curso.id'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'), nullable=False)
    monto_pagado = Column(Float, nullable=False)

    # Relaciones cruzadas usando back_populates
    curso = relationship("Curso", back_populates="inscripciones")
    estudiante = relationship("Estudiante", back_populates="inscripciones")

    def __repr__(self):
        return f"Inscripción #{self.id} - {self.curso.nombre}"
