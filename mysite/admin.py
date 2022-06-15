from django.contrib import admin
from .models import Job, Drawing, Document, Maker, Cutting, Machine, Qc, Painting, QcPainting , Assembly, Revise, File, AssemblyFile,PlanFile, ModelFile
# Register your models here.

admin.site.register(Job)
admin.site.register(Drawing)
admin.site.register(Document)
admin.site.register(Maker)
admin.site.register(Cutting)
admin.site.register(Machine)
admin.site.register(Qc)
admin.site.register(Painting)
admin.site.register(QcPainting)
admin.site.register(Assembly)
admin.site.register(Revise)
admin.site.register(File)
admin.site.register(AssemblyFile)
admin.site.register(PlanFile)
admin.site.register(ModelFile)