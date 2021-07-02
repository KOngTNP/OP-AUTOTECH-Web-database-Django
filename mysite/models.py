from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse
# Create your models here.

class Job(models.Model):
    jobNo = models.CharField(max_length=20, primary_key = True)
    projectName = models.CharField(max_length=80)
    projectDesc = models.TextField()

    class Meta:
        ordering=('-jobNo',)
    def __str__(self):
        return self.jobNo




class Drawing(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='drawingjob')
    drawingNo = models.CharField(max_length=40, primary_key = True)
    drawingDesc = models.TextField()
    Quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('date',)
    def __str__(self):
        return self.drawingNo



class Document(models.Model):
    drawing = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='documentdrawing')
    Quantity = models.IntegerField()
    user = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('date',)
    def __str__(self):
        return self.drawing