from django.db import models
from django.forms import ModelForm

from .models import Drawing, Job

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