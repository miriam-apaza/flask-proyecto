from flask_appbuilder import ModelView, GroupByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.group import aggregate_count
from .models import Area, Curso, Estudiante, Inscripcion
from app import appbuilder

# --- CRUDs Completos (Crear, Listar, Editar, Eliminar) por cada Tabla --- [cite: 40, 45]

class AreaView(ModelView):
    datamodel = SQLAInterface(Area)
    list_columns = ['nombre']

class CursoView(ModelView):
    datamodel = SQLAInterface(Curso)
    list_columns = ['nombre', 'costo', 'area']

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    list_columns = ['nombre_completo', 'correo']

class InscripcionView(ModelView):
    datamodel = SQLAInterface(Inscripcion)
    list_columns = ['id', 'estudiante', 'curso', 'fecha_inscripcion', 'monto_pagado']


# --- Reportes con Gráfica Dinámica (Conteo y Agrupación) --- [cite: 46, 51, 54]

class CursosPorAreaChartView(GroupByChartView):
    datamodel = SQLAInterface(Curso)
    chart_title = 'Distribución de Cursos por Área Académica'
    label_columns = CursoView.label_columns
    chart_type = 'PieChart'  # Define una gráfica dinámica de tipo pastel [cite: 56, 59]
    
    # Agrupación por la relación 'area' y conteo mediante la llave primaria 'id' [cite: 52, 54]
    group_by_columns = ['area']
    aggregate_by_columns = [('id', aggregate_count)]


# --- Registro de Vistas y Menús en la Interfaz General ---

# Seccion de Administración Académica
appbuilder.add_view(AreaView, "Áreas Académicas", icon="fa-th-list", category="Configuración")
appbuilder.add_view(CursoView, "Cursos Disponibles", icon="fa-book", category="Académico")
appbuilder.add_view(EstudianteView, "Registro de Alumnos", icon="fa-users", category="Académico")
appbuilder.add_view(InscripcionView, "Inscripciones y Pagos", icon="fa-graduation-cap", category="Académico")

# Sección de Reportes Estadísticos
appbuilder.add_view(CursosPorAreaChartView, "Cursos por Área", icon="fa-pie-chart", category="Estadísticas")