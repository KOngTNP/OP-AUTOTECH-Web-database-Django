from django.contrib import admin
from .models import Document, Job, Drawing, Maker
# Register your models here.

admin.site.register(Job)
admin.site.register(Drawing)
admin.site.register(Document)
admin.site.register(Maker)
