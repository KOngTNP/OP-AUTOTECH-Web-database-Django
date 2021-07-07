from django.contrib import admin
from .models import Job, Drawing, Document, Maker, Cutting, Machine
# Register your models here.

admin.site.register(Job)
admin.site.register(Drawing)
admin.site.register(Document)
admin.site.register(Maker)
admin.site.register(Cutting)
admin.site.register(Machine)
