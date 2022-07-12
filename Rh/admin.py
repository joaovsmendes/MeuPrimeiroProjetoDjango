from atexit import register
from msilib.schema import AdminUISequence
from django.contrib import admin

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'departamento','cargo']
    list_filter = ['departamento', 'cargo']

# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Departamento)