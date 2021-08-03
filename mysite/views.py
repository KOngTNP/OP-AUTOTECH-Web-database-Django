from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateJobForm,CreateDrawingForm,UpdateDrawingForm, UpdateJobForm, CreateDocumentForm, UpdateDocumentForm, CreateMakerForm, UpdateMakerForm,CreateCuttingForm, UpdateCuttingForm, CreateMachineForm, UpdateMachineForm, CreateQcForm, UpdateQcForm, CreatePaintingForm ,UpdatePaintingForm, CreateQcPaintingForm ,UpdateQcPaintingForm, CreateAssembyForm ,UpdateAssembyForm, CreateReviseForm ,UpdateReviseForm
from .models import Assemby, Job, Drawing, Document, Maker, Cutting, Machine, Qc, Painting, QcPainting, User, Revise
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import datetime


def homepage(request):
    return render(request,'home.html',{'text1':'wellcome to homepage','text2':'this is test homepage'})





def reportTable(request):
    first_person = Drawing.objects.raw(
        'SELECT "job_id" as "Job_number", "projectName" as "Project_name",\
        "drawingNo", "mysite_drawing"."Quantity" as "Drawing_QTY", "mysite_drawing"."datePublish" as "Drawing_date",\
        "mysite_document"."Quantity" as "Document_QTY", "mysite_document"."user_id" as "Document_user", "mysite_document"."datePublish" as "Document_date",\
        "mysite_maker"."name" as "Maker_name",\
        "mysite_cutting"."Quantity" as "Cutting_QTY", "mysite_cutting"."user_id" as "Cutting_user", "mysite_cutting"."datePublish" as "Cutting_date",\
        "mysite_machine"."Quantity" as "Machine_QTY", "mysite_machine"."user_id" as "Machine_user", "mysite_machine"."machineNum" as "Machine_number", "mysite_machine"."datePublish" as "Machine_date",\
        "mysite_qc"."Quantity" as "Qc_QTY", "mysite_qc"."user_id" as "Qc_user", "mysite_qc"."datePublish" as "Qc_date",\
        "mysite_painting"."name" as "Painting_name", "mysite_painting"."Quantity" as "Painting_QTY", "mysite_painting"."user_id" as "Painting_user", "mysite_painting"."datePublish" as "Painting_starting_date", "mysite_painting"."dateEnd" as "Painting_End_date",\
        "mysite_qcpainting"."Quantity" as "Qc_Painting_QTY", "mysite_qcpainting"."user_id" as "Qc_Painting_user", "mysite_qcpainting"."datePublish" as "Qc_Painting_date",\
        "mysite_assemby"."Quantity" as "Assemby_QTY", "mysite_assemby"."user_id" as "Assemby_user", "mysite_assemby"."datePublish" as "Assemby_date",\
        "mysite_revise"."numTimes" as "Revise_Times", "mysite_revise"."user_id" as "Revise_user", "mysite_revise"."reviseDesc" as "Revise_Description"\
        FROM mysite_job, mysite_drawing\
        LEFT JOIN mysite_document on  "drawingNo" = "mysite_document"."drawing_id"\
        LEFT JOIN mysite_maker on  "drawingNo" ="mysite_maker"."drawing_id"\
        LEFT JOIN mysite_cutting on  "drawingNo" ="mysite_cutting"."drawing_id"\
        LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id"\
        LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id" \
        LEFT JOIN mysite_assemby on  "drawingNo" ="mysite_assemby"."drawing_id"\
        LEFT JOIN mysite_revise on  "drawingNo" ="mysite_revise"."drawing_id"\
        WHERE "jobNo" = "job_id" ORDER BY "mysite_drawing"."datePublish"')
    get_user_id = User.objects.all
    return render(request,'reportTable.html',{'first_person':first_person, 'get_user_id':get_user_id})







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
        return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
    return render(request, 'drawing/editdrawing.html',{'get_drawing_id':get_drawing_id, 'get_job_id':get_job_id})






def workflow(request,drawing_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_maker_id = Maker.objects.get(drawing=get_drawing_id)
    except Maker.DoesNotExist:
        get_maker_id = None

    try:
        get_machine_id = Machine.objects.get(drawing=get_drawing_id)
    except Machine.DoesNotExist:
        get_machine_id = None

    try:
        get_painting_id = Painting.objects.get(drawing=get_drawing_id)
    except Painting.DoesNotExist:
        get_painting_id = None
    
    return render(request,'workflow.html',{'get_drawing_id':get_drawing_id, 'get_maker_id':get_maker_id, 'get_machine_id':get_machine_id, 'get_painting_id':get_painting_id})
 







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









def createMaker(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form = CreateMakerForm(request.POST)
        if form.is_valid():
            get_maker = form.save()
            
            if get_maker.name != 'OPAutotech':
                Cutting.objects.filter(drawing_id=get_drawing_id).delete()
                Machine.objects.filter(drawing_id=get_drawing_id).delete()
                Cutting.objects.create(drawing_id=get_drawing_id)
                Machine.objects.create(drawing_id=get_drawing_id)
                Cutting.objects.filter(drawing_id=get_drawing_id).update(user = None, Quantity = None, datePublish = None, dateUpdate = None)
                Machine.objects.filter(drawing_id=get_drawing_id).update(user = None, Quantity = None, machineNum = None, datePublish = None, dateUpdate = None)
            
            else:
                try:
                    get_cutting = Cutting.objects.filter(drawing_id=get_drawing_id)
                    get_cutting.delete()
                    get_machine = Machine.objects.filter(drawing_id=get_drawing_id)
                    get_machine.delete()
                except:
                    pass
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateMakerForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'maker/createmaker.html', { 'form':form, 'get_drawing_id':get_drawing_id })

def deleteMaker(reqest,drawing_id,maker_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_maker_id = Maker.objects.get(id=maker_id)
    get_maker_id.delete()
    Cutting.objects.filter(drawing_id=get_drawing_id).delete()
    Machine.objects.filter(drawing_id=get_drawing_id).delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editMaker(request,drawing_id,maker_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_maker_id = Maker.objects.get(id=maker_id)
    return render(request, 'maker/editmaker.html',{'get_drawing_id':get_drawing_id, 'get_maker_id':get_maker_id})


def updateMaker(request,drawing_id,maker_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_maker_id = get_object_or_404(Maker, pk=maker_id)
    form = UpdateMakerForm(request.POST, instance=get_maker_id)
    if form.is_valid:
        form.save()
        if form.is_valid():
            get_maker = form.save()
            if get_maker.name != 'OPAutotech':
                Cutting.objects.filter(drawing_id=get_drawing_id).delete()
                Machine.objects.filter(drawing_id=get_drawing_id).delete()
                Cutting.objects.create(drawing_id=drawing_id)
                Machine.objects.create(drawing_id=get_drawing_id)
                Cutting.objects.filter(drawing_id=drawing_id).update(user = None, Quantity = None, datePublish = None, dateUpdate = None)
                Machine.objects.filter(drawing_id=get_drawing_id).update(user = None, Quantity = None, machineNum = None, datePublish = None, dateUpdate = None)
            else:
                Cutting.objects.filter(drawing_id=get_drawing_id).delete()
                Machine.objects.filter(drawing_id=get_drawing_id).delete()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editMaker',{'get_drawing_id':get_drawing_id, 'get_maker_id':get_maker_id})









def createCutting(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form = CreateCuttingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateCuttingForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'cutting/createcutting.html', { 'form':form, 'get_drawing_id':get_drawing_id })

def deleteCutting(reqest,drawing_id,cutting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_cutting_id = Cutting.objects.get(id=cutting_id)
    get_cutting_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editCutting(request,drawing_id,cutting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_cutting_id = Cutting.objects.get(id=cutting_id)
    return render(request, 'cutting/editcutting.html',{'get_drawing_id':get_drawing_id, 'get_cutting_id':get_cutting_id})


def updateCutting(request,drawing_id,cutting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_cutting_id = get_object_or_404(Cutting, pk=cutting_id)
    form = UpdateCuttingForm(request.POST, instance=get_cutting_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editCutting',{'get_drawing_id':get_drawing_id, 'get_cutting_id':get_cutting_id})








def createMachine(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form = CreateMachineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateMachineForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'machine/createmachine.html', { 'form':form, 'get_drawing_id':get_drawing_id })

def deleteMachine(request,drawing_id,machine_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_machine_id = Machine.objects.get(id=machine_id)
    get_machine_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editMachine(request,drawing_id,machine_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_machine_id = Machine.objects.get(id=machine_id)
    return render(request, 'machine/editmachine.html',{'get_drawing_id':get_drawing_id, 'get_machine_id':get_machine_id})


def updateMachine(request,drawing_id,machine_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_machine_id = get_object_or_404(Machine, pk=machine_id)
    form = UpdateMachineForm(request.POST, instance=get_machine_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editMachine',{'get_drawing_id':get_drawing_id, 'get_machine_id':get_machine_id})







def createQc(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_cutting_id = get_object_or_404(Cutting, drawing_id=get_drawing_id)
    get_machine_id = get_object_or_404(Machine, drawing_id=get_drawing_id)
    if request.method == "POST":
        form  = CreateQcForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateQcForm(initial={'user':user})
    return render(request, 'qc/createqc.html', {'form':form, 'get_drawing_id':get_drawing_id, 'get_cutting_id':get_cutting_id, 'get_machine_id':get_machine_id})

def deleteQc(request,drawing_id,qc_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qc_id = Qc.objects.get(id=qc_id)
    get_qc_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editQc(request,drawing_id,qc_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qc_id = Qc.objects.get(id=qc_id)
    return render(request, 'qc/editqc.html',{'get_drawing_id':get_drawing_id, 'get_qc_id':get_qc_id})


def updateQc(request,drawing_id,qc_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qc_id = get_object_or_404(Qc, pk=qc_id)
    form = UpdateQcForm(request.POST, instance=get_qc_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editQc',{'get_drawing_id':get_drawing_id, 'get_qc_id':get_qc_id})






def createPainting(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form  = CreatePaintingForm(request.POST)
        if form.is_valid():
            form.save()
            Painting.objects.filter(drawing_id=get_drawing_id).update(dateEnd = None)

            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreatePaintingForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'painting/createpainting.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deletePainting(request,drawing_id,painting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_painting_id = Painting.objects.get(id=painting_id)
    get_painting_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))


def endPainting(request,drawing_id,painting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    Painting.objects.filter(drawing_id=get_drawing_id).update( dateEnd = datetime.datetime.now())
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editPainting(request,drawing_id,painting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_painting_id = Painting.objects.get(id=painting_id)
    return render(request, 'painting/editpainting.html',{'get_drawing_id':get_drawing_id, 'get_painting_id':get_painting_id})


def updatePainting(request,drawing_id,painting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_painting_id = get_object_or_404(Painting, pk=painting_id)
    form = UpdatePaintingForm(request.POST, instance=get_painting_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editPainting',{'get_drawing_id':get_drawing_id, 'get_painting_id':get_painting_id})







def createQcPainting(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_painting_id = get_object_or_404(Painting, drawing_id=get_drawing_id)
    if request.method == "POST":
        form  = CreateQcPaintingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateQcPaintingForm(initial={'user':user})
    return render(request, 'qcpainting/createqcpainting.html', {'form':form, 'get_drawing_id':get_drawing_id, 'get_painting_id':get_painting_id})

def deleteQcPainting(request,drawing_id,qcpainting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qcpainting_id = QcPainting.objects.get(id=qcpainting_id)
    get_qcpainting_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editQcPainting(request,drawing_id,qcpainting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qcpainting_id = QcPainting.objects.get(id=qcpainting_id)
    return render(request, 'qcpainting/editqcpainting.html',{'get_drawing_id':get_drawing_id, 'get_qcpainting_id':get_qcpainting_id})


def updateQcPainting(request,drawing_id,qcpainting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_qcpainting_id = get_object_or_404(QcPainting, pk=qcpainting_id)
    form = UpdateQcPaintingForm(request.POST, instance=get_qcpainting_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editQcPainting',{'get_drawing_id':get_drawing_id, 'get_qcpainting_id':get_qcpainting_id})








def createAssemby(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form  = CreateAssembyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateAssembyForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'assemby/createassemby.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deleteAssemby(request,drawing_id,assemby_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_assemby_id = Assemby.objects.get(id=assemby_id)
    get_assemby_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editAssemby(request,drawing_id,assemby_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_assemby_id = Assemby.objects.get(id=assemby_id)
    return render(request, 'assemby/editassemby.html',{'get_drawing_id':get_drawing_id, 'get_assemby_id':get_assemby_id})


def updateAssemby(request,drawing_id,assemby_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_assemby_id = get_object_or_404(Assemby, pk=assemby_id)
    form = UpdateAssembyForm(request.POST, instance=get_assemby_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editAssemby',{'get_drawing_id':get_drawing_id, 'get_assemby_id':get_assemby_id})







def createRevise(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.method == "POST":
        form  = CreateReviseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = CreateReviseForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'revise/createrevise.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deleteRevise(request,drawing_id,revise_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_revise_id = Revise.objects.get(id=revise_id)
    get_revise_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editRevise(request,drawing_id,revise_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_revise_id = Revise.objects.get(id=revise_id)
    numTimes = get_revise_id.numTimes + 1
    return render(request, 'revise/editrevise.html',{'get_drawing_id':get_drawing_id, 'get_revise_id':get_revise_id, 'numTimes':numTimes})


def updateRevise(request,drawing_id,revise_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_revise_id = get_object_or_404(Revise, pk=revise_id)
    form = UpdateReviseForm(request.POST, instance=get_revise_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editRevise',{'get_drawing_id':get_drawing_id, 'get_revise_id':get_revise_id})
