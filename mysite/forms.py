from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import  Job, Drawing, Document, Maker, Cutting, Machine, Qc

class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

class UpdateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['projectName', 'projectDesc']




class CreateDrawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = "__all__"
        
class UpdateDrawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['drawingNo', 'drawingDesc', 'Quantity']




class CreateDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"

class UpdateDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['Quantity']



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
        fields = ['Quantity', 'machineNum']



class CreateQcForm(ModelForm):
    class Meta:
        model = Qc
        fields = "__all__"


class UpdateQcForm(ModelForm):
    class Meta:
        model = Qc
        fields = ['Quantity']

#     def __init__(self, *args, **kwargs):
#         super(MyCustomForm, self).__init__(*args, **kwargs)        
#         self.fields['country'] = forms.ChoiceField(choices=[('1','india'),('2','US')])
#         self.fields['state'].queryset = State.objects.filter(pk=2)



# display123 = Job.objects.get(jobNo=job_id)
    

# class MyCustomForm(forms.ModelForm):
#     class Meta:
#         model = MyCustomModal
#         fields = [
#             'country',
#             'state',           
#         ]        

#     def __init__(self, *args, **kwargs):
#         super(MyCustomForm, self).__init__(*args, **kwargs)        
#         self.fields['country'] = forms.ChoiceField(choices=[('1','india'),('2','US')])
#         self.fields['state'].queryset = State.objects.filter(pk=2)