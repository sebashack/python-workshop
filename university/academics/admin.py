from django.contrib import admin
from academics.models import Carrera, Estudiante, Curso, Matricula


admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)
