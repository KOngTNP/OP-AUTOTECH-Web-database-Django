from django.shortcuts import render, redirect
from .forms import CreateJobForm,CreateDrawingForm,UpdateDrawingForm, UpdateJobForm ,CreateDocumentForm ,UpdateDocumentForm
from .models import Job, Drawing, Document, Maker
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

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


def jobTable(request):
    #Query Data from model
    search_job = request.GET.get('search')
    if search_job:
        data = Job.objects.filter(Q(jobNo__icontains=search_job) & Q(jobNo__icontains=search_job))
        if str(data) == '<QuerySet []>':
            data = Job.objects.filter(Q(projectName__icontains=search_job) & Q(projectName__icontains=search_job))
    else:
        data = Job.objects.all()

    return render(request,'job/jobTable.html',{'jobs':data})

def createJob(request):
    user = request.user
    if request.method == "POST":
        form = CreateJobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/jobTable")
    else:
        form = CreateJobForm(initial={'user': user})
    return render(request,'job/createJob.html', {'form': form})

def deleteJob(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_job_id.delete()
    data = Job.objects.all()
    return redirect("/jobTable",{'jobs':data})

def editJob(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    return render(request,'job/editjob.html',{'jobs':get_job_id})

def updateJob(request,job_id):
    data = Job.objects.all()
    get_job_id = Job.objects.get(jobNo=job_id)
    form = UpdateJobForm(request.POST, instance=get_job_id)
    if form.is_valid():
        form.save()
        # messages.success(request,"Record Updated Successfull!")
        return redirect("/jobTable",{'jobs':data})
        









def allDrawing(request):
    #Query Data from model
    search_drawing = request.GET.get('search')
    if search_drawing:
        data = Drawing.objects.filter(Q(drawingNo__icontains=search_drawing) & Q(drawingNo__icontains=search_drawing))
        if str(data) == '<QuerySet []>':
            data = Drawing.objects.filter(Q(drawingDesc__icontains=search_drawing) & Q(drawingDesc__icontains=search_drawing))
    else:
        data = Drawing.objects.all()
    return render(request,'drawing/allDrawing.html',{'drawing':data})
        









def drawingTable(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    return render(request,'drawing/drawingTable.html',{'get_job_id':get_job_id})

def createDrawing(request,job_id):
    user = request.user
    get_job_id = Job.objects.get(jobNo=job_id)
    if request.method == "POST":
        form = CreateDrawingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
            
    else:
        form = CreateDrawingForm(initial={'job': get_job_id, 'user': user})
    return render(request, 'drawing/createDrawing.html', {'form': form, 'get_job_id':get_job_id})

def deleteDrawing(request,job_id,drawing_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_drawing_id.delete()
    return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))

def editDrawing(request,job_id,drawing_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    return render(request, 'drawing/editdrawing.html',{'get_drawing_id':get_drawing_id, 'get_job_id':get_job_id})


def updateDrawing(request,job_id,drawing_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_drawing_id = get_object_or_404(Drawing, pk=drawing_id)
    form = UpdateDrawingForm(request.POST, instance=get_drawing_id)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfull!")
        # return render(request,'drawing/drawingTable.html',{'get_job_id':get_job_id})
        return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
    return render(request, 'drawing/editdrawing.html',{'get_drawing_id':get_drawing_id, 'get_job_id':get_job_id})






def workflow(request,drawing_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    print(get_drawing_id)
    return render(request,'workflow.html',{'get_drawing_id':get_drawing_id})








def createDocument(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form = CreateDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateDocumentForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'document/createDocument.html', { 'form':form, 'get_drawing_id':get_drawing_id })

def deleteDocument(request,drawing_id,document_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_document_id = Document.objects.get(id=document_id)
    get_document_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editDocument(request,drawing_id,document_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_document_id = Document.objects.get(id=document_id)
    return render(request, 'document/editDocument.html',{'get_drawing_id':get_drawing_id, 'get_document_id':get_document_id})

def updateDocument(request,drawing_id,document_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_document_id = get_object_or_404(Document, pk=document_id)
    form = UpdateDocumentForm(request.POST, instance=get_document_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editDocument',{'get_drawing_id':get_drawing_id, 'get_document_id':get_document_id})

