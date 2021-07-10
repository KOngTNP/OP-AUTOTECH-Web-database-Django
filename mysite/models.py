from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, DateTimeField, related
from django.forms.widgets import DateInput
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    jobNo = models.CharField(max_length=20, primary_key=True)
    projectName = models.CharField(max_length=80)
    projectDesc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)


    datePublish = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.jobNo




class Drawing(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='drawingjob')
    drawingNo = models.CharField(max_length=40, primary_key = True)
    drawingDesc = models.TextField()
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('drawingNo','datePublish')
    def __str__(self):
        return self.drawingNo

# 1
class Document(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='documentdrawing')
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.drawing
# 2
class Maker(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='makerdrawing')

    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.drawing

# 3
class Cutting(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='cuttingdrawing')

    Quantity = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)

# 4
class Machine(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='machinedrawing')

    Quantity = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    machineNum = models.IntegerField()

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.drawing
# 5
class Qc(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='qcdrawing')

    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.drawing

# 6
# **********************************************************************************************************************************
class Painting(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='paintingdrawing')

    name = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateEnd = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)
    # ...


# **********************************************************************************************************************************

# 7
class QcPainting(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='qcpaintingdrawing')

    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.drawing

# 8
class Assemby(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='assembydrawing')
    
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    datePublish = models.DateTimeField(auto_now_add=True, null=True)
    dateUpdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.drawing
