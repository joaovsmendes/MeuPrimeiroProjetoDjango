from atexit import register
from msilib.schema import AdminUISequence
from django.contrib import admin

from Rh.models import Funcionario
from Rh.models import Departamento

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Departamento)
