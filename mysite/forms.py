from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import  Job, Drawing, Document, Maker, Cutting, Machine, Qc ,Painting, QcPainting, Assembly, Revise, File, AssemblyFile

class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

class UpdateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['projectName']




class CreateDrawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = "__all__"
        
class UpdateDrawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['drawingNo', 'Quantity']




class CreateDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"

class UpdateDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['Quantity','skipAssembly']



class CreateMakerForm(ModelForm):
    class Meta:
        model = Maker
        fields = "__all__"


class UpdateMakerForm(ModelForm):
    class Meta:
        model = Maker
        fields = ['name']



class CreateCuttingForm(ModelForm):
    class Meta:
        model = Cutting
        fields = "__all__"


class UpdateCuttingForm(ModelForm):
    class Meta:
        model = Cutting
        fields = ['Quantity']




class CreateMachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"


class UpdateMachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = ['Quantity']



class CreateQcForm(ModelForm):
    class Meta:
        model = Qc
        fields = "__all__"


class UpdateQcForm(ModelForm):
    class Meta:
        model = Qc
        fields = ['Quantity']


class CreatePaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = "__all__"


class UpdatePaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['Quantity','name']



class CreateQcPaintingForm(ModelForm):
    class Meta:
        model = QcPainting
        fields = "__all__"


class UpdateQcPaintingForm(ModelForm):
    class Meta:
        model = QcPainting
        fields = ['Quantity']



class CreateAssemblyForm(ModelForm):
    class Meta:
        model = Assembly
        fields = "__all__"


class UpdateAssemblyForm(ModelForm):
    class Meta:
        model = Assembly
        fields = ['Quantity']


class CreateReviseForm(ModelForm):
    class Meta:
        model = Revise
        fields = "__all__"

class UpdateReviseForm(ModelForm):
    class Meta:
        model = Revise
        fields = ['numTimes', 'reviseDesc']


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = "__all__"

class UploadAssemblyFileForm(ModelForm):
    class Meta:
        model = AssemblyFile
        fields = "__all__"