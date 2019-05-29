from django.contrib import admin
from faculdade.models import Professor
from faculdade.models import Disciplina
from faculdade.models import Aluno
from faculdade.models import Matricula
from faculdade.models import Alocacao
# Register your models here.
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Matricula)
admin.site.register(Alocacao)