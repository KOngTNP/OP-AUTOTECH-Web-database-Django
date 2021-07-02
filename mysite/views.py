from django import forms
from django.db.models.base import Model
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView ,DetailView
from .forms import CreateJobForm,CreateDrawingForm
from .models import Job, Drawing


def homepage(request):
    #                                   ชื่อ      ข้อความ
    # return render(request,'index.html',{'name':'test'})
    tags=['1','2','3','4']
    rating=3
    return render(request,'home.html',
    {
        'text1':'wellcome to homepage',
        'text2':'this is test homepage',
        'tag':tags,
        'rating':rating
    })





def createJob(request):
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/jobTable")
    else:
        form = CreateJobForm()
    return render(request,'createJob.html', {'form': form})

def jobTable(request):
    #Query Data from model
    data = Job.objects.all()
    return render(request,'jobTable.html',{'jobs':data})





def createDrawing(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    if request.method == "POST":
        form = CreateDrawingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'drawingTable.html',{'get_job_id':get_job_id})
    else:
        form = CreateDrawingForm(initial={'job': get_job_id})
    return render(request, 'createDrawing.html', {'form': form, 'get_job_id':get_job_id})

def drawingTable(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    return render(request,'drawingTable.html',{'get_job_id':get_job_id})


# def delete(request,job_id):
#     get_job_id = Job.objects.get(jobNo=job_id)
#     get_job_id.delete()
#     data = Job.objects.all()
#     return render(request,'jobTable.html',{'jobs':data})


def workflow(request,drawing_no):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_no)
    return render(request, 'workflow.html' ,{'get_drawing_id':get_drawing_id})