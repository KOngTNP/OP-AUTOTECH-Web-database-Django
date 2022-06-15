from functools import total_ordering
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateJobForm,CreateDrawingForm,UpdateDrawingForm, UpdateJobForm, CreateDocumentForm, UpdateDocumentForm, CreateMakerForm, UpdateMakerForm,CreateCuttingForm, UpdateCuttingForm, CreateMachineForm, UpdateMachineForm, CreateQcForm, UpdateQcForm, CreatePaintingForm ,UpdatePaintingForm, CreateQcPaintingForm ,UpdateQcPaintingForm, CreateAssemblyForm ,UpdateAssemblyForm, CreateReviseForm ,UpdateReviseForm, UploadFileForm, UploadAssemblyFileForm, UploadPlanFileForm, UploadModelFileForm
from .models import Assembly, Job, Drawing, Document, Maker, Cutting, Machine, Qc, Painting, QcPainting, User, Revise, File, AssemblyFile,PlanFile, ModelFile
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.db.models import Q
import datetime
from datetime import date
import os


def homepage(request):
    return render(request,'home.html',{'text1':'wellcome to homepage','text2':'this is test homepage'})





def reportTable(request):
    current_week = date.today().isocalendar()[1] 
    current_month = datetime.datetime.now().month
    select_all_report = Drawing.objects.raw(
        'SELECT "job_id" as "Job_number", "projectName" as "Project_name",\
        "drawingNo", "mysite_drawing"."Quantity" as "Drawing_QTY", "mysite_drawing"."datePublish" as "Drawing_date",\
        "mysite_document"."Quantity" as "Document_QTY", "mysite_document"."user_id" as "Document_user", "mysite_document"."datePublish" as "Document_date",\
        "mysite_maker"."name" as "Maker_name",\
        "mysite_cutting"."Quantity" as "Cutting_QTY", "mysite_cutting"."user_id" as "Cutting_user", "mysite_cutting"."datePublish" as "Cutting_date",\
        "mysite_machine"."Quantity" as "Machine_QTY", "mysite_machine"."user_id" as "Machine_user", "mysite_machine"."datePublish" as "Machine_date",\
        "mysite_qc"."Quantity" as "Qc_QTY", "mysite_qc"."user_id" as "Qc_user", "mysite_qc"."datePublish" as "Qc_date",\
        "mysite_painting"."name" as "Painting_name", "mysite_painting"."Quantity" as "Painting_QTY", "mysite_painting"."user_id" as "Painting_user", "mysite_painting"."datePublish" as "Painting_starting_date", "mysite_painting"."dateEnd" as "Painting_End_date",\
        "mysite_qcpainting"."Quantity" as "Qc_Painting_QTY", "mysite_qcpainting"."user_id" as "Qc_Painting_user", "mysite_qcpainting"."datePublish" as "Qc_Painting_date",\
        "mysite_assembly"."Quantity" as "Assembly_QTY", "mysite_assembly"."user_id" as "Assembly_user", "mysite_assembly"."datePublish" as "Assembly_date",\
        "mysite_revise"."numTimes" as "Revise_Times", "mysite_revise"."user_id" as "Revise_user", "mysite_revise"."reviseDesc" as "Revise_Description"\
        FROM mysite_job, mysite_drawing\
        LEFT JOIN mysite_document on  "drawingNo" = "mysite_document"."drawing_id"\
        LEFT JOIN mysite_maker on  "drawingNo" ="mysite_maker"."drawing_id"\
        LEFT JOIN mysite_cutting on  "drawingNo" ="mysite_cutting"."drawing_id"\
        LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id"\
        LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id" \
        LEFT JOIN mysite_assembly on  "drawingNo" ="mysite_assembly"."drawing_id"\
        LEFT JOIN mysite_revise on  "drawingNo" ="mysite_revise"."drawing_id"\
        WHERE "jobNo" = "job_id" ORDER BY "mysite_drawing"."datePublish"')

    document_related = Document.objects.select_related('user','drawing')
    cutting_related = Cutting.objects.select_related('user','drawing')
    machine_related = Machine.objects.select_related('user','drawing')
    qc_related = Qc.objects.select_related('user','machine','cutting')
    painting_related = Painting.objects.select_related('user','drawing')
    qcpainting_related = QcPainting.objects.select_related('user','painting')
    assembly_related = Assembly.objects.select_related('user','drawing')

    document_week_report = document_related.filter(datePublish__week=current_week)
    count_document_week_report = 0
    qty_document_week_report = 0
    for dwr in document_week_report:
        count_document_week_report += 1
        qty_document_week_report += dwr.Quantity

    document_month_report = document_related.filter(datePublish__month=current_month)
    count_document_month_report = 0
    qty_document_month_report = 0
    for dmr in document_month_report:
        count_document_month_report += 1
        qty_document_month_report += dmr.Quantity

    cutting_week_report = cutting_related.filter(datePublish__week=current_week)
    count_cutting_week_report = 0
    qty_cutting_week_report = 0
    for cwr in cutting_week_report:
        count_cutting_week_report += 1
        qty_cutting_week_report += cwr.Quantity

    cutting_month_report = cutting_related.filter(datePublish__month=current_month)
    count_cutting_month_report = 0
    qty_cutting_month_report = 0
    for cmr in cutting_month_report:
        count_cutting_month_report += 1
        qty_cutting_month_report += cmr.Quantity


    machine_week_report = machine_related.filter(datePublish__week=current_week)
    count_machine_week_report = 0
    qty_machine_week_report = 0
    for mwr in machine_week_report:
        count_machine_week_report += 1
        qty_machine_week_report += mwr.Quantity

    machine_month_report = machine_related.filter(datePublish__month=current_month)
    count_machine_month_report = 0
    qty_machine_month_report = 0
    for mmr in machine_month_report:
        count_machine_month_report += 1
        qty_machine_month_report += mmr.Quantity

    qc_week_report = qc_related.filter(datePublish__week=current_week)
    count_qc_week_report = 0
    qty_qc_week_report = 0
    for qwr in qc_week_report:
        count_qc_week_report += 1
        qty_qc_week_report += qwr.Quantity

    qc_month_report = qc_related.filter(datePublish__month=current_month)
    count_qc_month_report = 0
    qty_qc_month_report = 0
    for qmr in qc_month_report:
        count_qc_month_report += 1
        qty_qc_month_report += qmr.Quantity

    painting_week_report = painting_related.filter(datePublish__week=current_week)
    count_painting_week_report = 0
    qty_painting_week_report = 0
    for pwr in painting_week_report:
        count_painting_week_report += 1
        qty_painting_week_report += pwr.Quantity

    painting_month_report = painting_related.filter(datePublish__month=current_month)
    count_painting_month_report = 0
    qty_painting_month_report = 0
    for pmr in painting_month_report:
        count_painting_month_report += 1
        qty_painting_month_report += pmr.Quantity


    qcpainting_week_report = qcpainting_related.filter(datePublish__week=current_week)
    count_qcpainting_week_report = 0
    qty_qcpainting_week_report = 0
    for qpwr in qcpainting_week_report:
        count_qcpainting_week_report += 1
        qty_qcpainting_week_report += qpwr.Quantity

    qcpainting_month_report = qcpainting_related.filter(datePublish__month=current_month)
    count_qcpainting_month_report = 0
    qty_qcpainting_month_report = 0
    for qpmr in qcpainting_month_report:
        count_qcpainting_month_report += 1
        qty_qcpainting_month_report += qpmr.Quantity


    assembly_week_report = assembly_related.filter(datePublish__week=current_week)
    count_assembly_week_report = 0
    qty_assembly_week_report = 0
    for awr in assembly_week_report:
        count_assembly_week_report += 1
        qty_assembly_week_report += awr.Quantity

    assembly_month_report = assembly_related.filter(datePublish__month=current_month)
    count_assembly_month_report = 0
    qty_assembly_month_report = 0
    for amr in assembly_month_report:
        count_assembly_month_report += 1
        qty_assembly_month_report += amr.Quantity

    search_date = request.GET.get('search')
    if search_date:
        document_search = document_related.filter(datePublish__date=search_date)
        cutting_search = cutting_related.filter(datePublish__date=search_date)
        machine_search = machine_related.filter(datePublish__date=search_date)
        qc_search = qc_related.filter(datePublish__date=search_date)
        painting_search = painting_related.filter(dateEnd__date=search_date)
        qcpainting_search = qcpainting_related.filter(datePublish__date=search_date)
        assembly_search = assembly_related.filter(datePublish__date=search_date)
    else:
        document_search = document_related.filter(datePublish__date=datetime.date.today())
        cutting_search = cutting_related.filter(datePublish__date=datetime.date.today())
        machine_search = machine_related.filter(datePublish__date=datetime.date.today())
        qc_search = qc_related.filter(datePublish__date=datetime.date.today())
        painting_search = painting_related.filter(dateEnd__date=datetime.date.today())
        qcpainting_search = qcpainting_related.filter(datePublish__date=datetime.date.today())
        assembly_search = assembly_related.filter(datePublish__date=datetime.date.today())

    count_document_qty = 0
    count_document = len(document_search)
    for document in document_search:
        count_document_qty += document.Quantity

    
    count_cutting_qty = 0
    count_cutting = len(cutting_search)
    for cutting in cutting_search:
        count_cutting_qty += cutting.Quantity

    count_machine_qty = 0
    count_machine = len(machine_search)
    for machine in machine_search:
        count_machine_qty += machine.Quantity

    
    count_qc_qty = 0
    count_qc = len(qc_search)
    for qc in qc_search:
        count_qc_qty += qc.Quantity

    
    count_painting_qty = 0
    count_painting = len(painting_search)
    for painting in painting_search:
        count_painting_qty += painting.Quantity

    
    count_qcpainting_qty = 0
    count_qcpainting = len(qcpainting_search)
    for qcpainting in qcpainting_search:
        count_qcpainting_qty += qcpainting.Quantity

    
    count_assembly_qty = 0
    count_assembly = len(assembly_search)
    for assembly in assembly_search:
        count_assembly_qty += assembly.Quantity

    return render(request,'reportTable.html',
    {
        'select_all_report':select_all_report,
        'document_week_report':document_week_report, 'document_month_report':document_month_report,
        'cutting_week_report':cutting_week_report, 'cutting_month_report':cutting_month_report,
        'machine_week_report':machine_week_report, 'machine_month_report':machine_month_report,
        'qc_week_report':qc_week_report, 'qc_month_report':qc_month_report,
        'painting_week_report':painting_week_report, 'painting_month_report':painting_month_report,
        'qcpainting_week_report':qcpainting_week_report, 'qcpainting_month_report':qcpainting_month_report,
        'assembly_week_report':assembly_week_report, 'assembly_month_report':assembly_month_report,
        'document_search':document_search, 'cutting_search':cutting_search, 'machine_search':machine_search, 'qc_search':qc_search, 'painting_search':painting_search, 'qcpainting_search':qcpainting_search, 'assembly_search':assembly_search,
        'count_document_qty':count_document_qty, 'count_cutting_qty':count_cutting_qty, 'count_machine_qty':count_machine_qty, 'count_qc_qty':count_qc_qty, 'count_painting_qty':count_painting_qty, 'count_qcpainting_qty':count_qcpainting_qty, 'count_assembly_qty':count_assembly_qty,
        'count_document':count_document, 'count_cutting':count_cutting, 'count_machine':count_machine, 'count_qc':count_qc, 'count_painting':count_painting, 'count_qcpainting':count_qcpainting, 'count_assembly':count_assembly,
        'search_date':search_date,
        'count_document_week_report':count_document_week_report, 'count_cutting_week_report':count_cutting_week_report, 'count_machine_week_report':count_machine_week_report, 'count_qc_week_report':count_qc_week_report, 'count_painting_week_report':count_painting_week_report, 'count_qcpainting_week_report':count_qcpainting_week_report, 'count_assembly_week_report':count_assembly_week_report,
        'qty_document_week_report':qty_document_week_report, 'qty_cutting_week_report':qty_cutting_week_report, 'qty_machine_week_report':qty_machine_week_report, 'qty_qc_week_report':qty_qc_week_report, 'qty_painting_week_report':qty_painting_week_report, 'qty_qcpainting_week_report':qty_qcpainting_week_report, 'qty_assembly_week_report':qty_assembly_week_report,
        'count_document_month_report':count_document_month_report, 'count_cutting_month_report':count_cutting_month_report, 'count_machine_month_report':count_machine_month_report, 'count_qc_month_report':count_qc_month_report, 'count_painting_month_report':count_painting_month_report, 'count_qcpainting_month_report':count_qcpainting_month_report, 'count_assembly_month_report':count_assembly_month_report,
        'qty_document_month_report':qty_document_month_report, 'qty_cutting_month_report':qty_cutting_month_report, 'qty_machine_month_report':qty_machine_month_report, 'qty_qc_month_report':qty_qc_month_report, 'qty_painting_month_report':qty_painting_month_report, 'qty_qcpainting_month_report':qty_qcpainting_month_report, 'qty_assembly_month_report':qty_assembly_month_report,
    })


def realtimeReport(request):
    this_year = datetime.datetime.now().year

    qty_document = 0
    count_document = 0
    document = Document.objects.filter(datePublish__date=datetime.date.today())
    for document in document:
        qty_document += document.Quantity
        count_document += 1
    qty_document_year = 0
    count_document_year = 0
    document_year = Drawing.objects.filter(datePublish__year=this_year)
    for document_year in document_year:
        qty_document_year += document_year.Quantity
        count_document_year += 1
    

    qty_cutting = 0
    count_cutting = 0
    cutting = Cutting.objects.filter(datePublish__date=datetime.date.today()).exclude(user__username = 'othercompany')
    for cutting in cutting:
        qty_cutting += cutting.Quantity
        count_cutting += 1

    qty_machine = 0
    count_machine = 0
    machine = Machine.objects.filter(datePublish__date=datetime.date.today()).exclude(user__username = 'othercompany')
    for machine in machine:
        qty_machine += machine.Quantity
        count_machine += 1
    qty_machine_year = 0
    count_machine_year = 0
    machine_year = Machine.objects.filter(datePublish__year=this_year)
    for machine_year in machine_year:
        qty_machine_year += machine_year.Quantity
        count_machine_year += 1
    

    qty_qc = 0
    count_qc = 0
    qc = Qc.objects.filter(datePublish__date=datetime.date.today())
    for qc in qc:
        qty_qc += qc.Quantity
        count_qc += 1

    qty_painting = 0
    count_painting = 0
    painting = Painting.objects.filter(datePublish__date=datetime.date.today())
    painting = painting.exclude(dateEnd=None)
    for painting in painting:
        qty_painting += painting.Quantity
        count_painting += 1

    qty_assembly = 0
    count_assembly = 0
    assembly = Assembly.objects.filter(datePublish__date=datetime.date.today())
    for assembly in assembly:
        qty_assembly += assembly.Quantity
        count_assembly += 1
    qty_assembly_year = 0
    count_assembly_year = 0
    assembly_year = Assembly.objects.filter(datePublish__year=this_year)
    for assembly_year in assembly_year:
        qty_assembly_year += assembly_year.Quantity
        count_assembly_year += 1

    return render(request,'realtimeReport.html',
    {
        'count_document':count_document,'qty_document': qty_document, 'qty_document_year':qty_document_year, 'count_document_year':count_document_year,
        'count_cutting':count_cutting,'qty_cutting': qty_cutting,
        'count_machine':count_machine,'qty_machine': qty_machine, 'qty_machine_year':qty_machine_year, 'count_machine_year':count_machine_year,
        'count_qc':count_qc,'qty_qc': qty_qc,
        'count_painting':count_painting,'qty_painting': qty_painting,
        'count_assembly':count_assembly,'qty_assembly': qty_assembly, 'qty_assembly_year':qty_assembly_year, 'count_assembly_year':count_assembly_year,
    })




def jobTable(request):
    #Query Data from model
    search_job = request.GET.get('search')
    sum_job = len(Job.objects.select_related('user'))
    if search_job:
        data = Job.objects.filter(Q(jobNo__icontains=search_job) & Q(jobNo__icontains=search_job))
        if str(data) == '<QuerySet []>':
            data = Job.objects.filter(Q(projectName__icontains=search_job) & Q(projectName__icontains=search_job))
    else:
        data = Job.objects.select_related('user')
    all_qty = Job.objects.raw('SELECT "mysite_job"."jobNo", sum("mysite_drawing"."Quantity") as "QTY" FROM mysite_drawing , mysite_job WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" GROUP BY "mysite_job"."jobNo"')
    done_qty = Job.objects.raw('SELECT "mysite_job"."jobNo" as "jobNo", sum("mysite_assembly"."Quantity") as "Assembly_QTY" FROM mysite_job, mysite_drawing LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" GROUP BY "mysite_job"."jobNo"')
    sum_drawing = len(Drawing.objects.select_related('job'))
    all_percent = Job.objects.raw('SELECT "mysite_job"."jobNo" as "jobNo", ( sum((coalesce("mysite_document"."Quantity", 0)) + (coalesce("mysite_cutting"."Quantity", 0)) + (coalesce("mysite_machine"."Quantity", 0)) + (coalesce("mysite_qc"."Quantity", 0)) + (coalesce("mysite_painting"."Quantity", 0)) + (coalesce("mysite_assembly"."Quantity", 0)) + (coalesce("mysite_qcpainting"."Quantity", 0)))*100) / (sum("mysite_drawing"."Quantity")*7) as "Percent" \
        FROM mysite_job, mysite_drawing\
        LEFT JOIN mysite_document on "drawingNo" ="mysite_document"."drawing_id" \
        LEFT JOIN mysite_cutting on "drawingNo" ="mysite_cutting"."drawing_id" \
        LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id"\
        LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id"\
        LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" \
        WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" \
        GROUP BY "mysite_job"."jobNo"')
    sum_all = 0
    for all in all_qty:
        sum_all += all.QTY
    return render(request,'job/jobTable.html',{'jobs':data, 'all_qty':all_qty, 'done_qty':done_qty, "sum_drawing":sum_drawing, "sum_job":sum_job, "sum_all":sum_all , "all_percent":all_percent})

def jobReport(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    all_qty = Job.objects.raw('SELECT "mysite_job"."jobNo" as "jobNo", sum("mysite_drawing"."Quantity") as "QTY",\
        sum("mysite_document"."Quantity") as "Document_QTY",\
        sum("mysite_cutting"."Quantity") as "Cutting_QTY" ,\
        sum("mysite_machine"."Quantity") as "Machine_QTY" ,\
        sum("mysite_qc"."Quantity") as "Qc_QTY" ,\
        sum("mysite_painting"."Quantity") as "Painting_QTY" ,\
        sum("mysite_qcpainting"."Quantity") as "PaintingQc_QTY" ,\
        sum("mysite_assembly"."Quantity") as "Assembly_QTY"\
        FROM mysite_job, mysite_drawing\
        LEFT JOIN mysite_document on "drawingNo" ="mysite_document"."drawing_id" \
        LEFT JOIN mysite_cutting on "drawingNo" ="mysite_cutting"."drawing_id" \
        LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id"\
        LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id"\
        LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" \
        WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" \
        GROUP BY "mysite_job"."jobNo"')
    for all in all_qty:
        if get_job_id.jobNo == all.jobNo:
            if all.QTY != None:
                percent = (100/all.QTY)
            else:
                percent = f'{0:.2f}'
            if all.Document_QTY != None:
                perDocument = f'{percent*all.Document_QTY:.2f}'
            else:
                perDocument = f'{0:.2f}'
            if all.Cutting_QTY != None:
                perCutting = f'{percent*all.Cutting_QTY:.2f}'
            else:
                perCutting = f'{0:.2f}'
            if all.Machine_QTY != None:
                perMachine = f'{percent*all.Machine_QTY:.2f}'
            else:
                perMachine = f'{0:.2f}'
            if all.Qc_QTY != None:
                perQc = f'{percent*all.Qc_QTY:.2f}'
            else: 
                perQc = f'{0:.2f}'
            if all.Painting_QTY != None:
                perPainting = f'{percent*all.Painting_QTY:.2f}'
            else:
                perPainting = f'{0:.2f}'
            if all.PaintingQc_QTY != None:
                perPaintingQc = f'{percent*all.PaintingQc_QTY:.2f}'
            else:
                perPaintingQc = f'{0:.2f}'
            if all.Assembly_QTY != None:
                perAssembly = f'{percent*all.Assembly_QTY:.2f}'
            else:
                perAssembly = f'{0:.2f}'

    return render(request, 'job/jobreport.html',{'get_job_id':get_job_id, 'all_qty':all_qty, 'perDocument':perDocument, 'perCutting':perCutting, 'perMachine':perMachine, 'perQc':perQc, 'perPainting':perPainting, 'perPaintingQc':perPaintingQc, 'perAssembly':perAssembly})

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
    if str(request.user.username) == str(get_job_id.user) or request.user.is_superuser or request.user.is_staff:
        try:
            try:
                get_assemblyfile_id = AssemblyFile.objects.get(job = job_id)
                get_assemblyfile_id.delete()
            except:
                pass
            try:
                get_planfile_id = PlanFile.objects.get(job = job_id)
                get_planfile_id.delete()
            except:
                pass
            try:
                get_modelfile_id = ModelFile.objects.get(job = job_id)
                get_modelfile_id.delete()
            except:
                pass
            get_drawing_id = Drawing.objects.get(job_id=get_job_id)
            get_file_id = File.objects.get(drawing_id = get_drawing_id)
            get_file_id.delete()
            get_job_id.delete()
        except:
            get_job_id.delete()
    data = Job.objects.select_related('user')
    return redirect("/jobTable",{'jobs':data})

def editJob(request,job_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    return render(request,'job/editjob.html',{'jobs':get_job_id})

def updateJob(request,job_id):
    data = Job.objects.select_related('user')
    get_job_id = Job.objects.get(jobNo=job_id)
    form = UpdateJobForm(request.POST, instance=get_job_id)
    if form.is_valid():
        form.save()
        # messages.success(request,"Record Updated Successfull!")
        return redirect("/jobTable",{'jobs':data})
        






def drawingTable(request,job_id):
    get_drawing_all = Drawing.objects.select_related('job','user')
    get_drawing = get_drawing_all.filter(job = job_id)
    get_fileassembly_all = AssemblyFile.objects.select_related('job','user')
    get_fileassembly = get_fileassembly_all.filter(job = job_id)

    get_fileplan_all = PlanFile.objects.select_related('job','user')
    get_fileplan = get_fileplan_all.filter(job = job_id)

    get_filemodel_all = ModelFile.objects.select_related('job','user')
    get_filemodel = get_filemodel_all.filter(job = job_id)
    count_drawing = len(get_drawing)
    count_drawing_qty = 0
    for drawing in get_drawing:
        count_drawing_qty += drawing.Quantity
    done_qty = "None"
    # done_qty = Drawing.objects.raw(
    # 'SELECT "mysite_drawing"."drawingNo" as "drawingNo", "mysite_document"."Quantity" as "Document_QTY", \
    # "mysite_cutting"."Quantity" as "Cutting_QTY", "mysite_machine"."Quantity" as "Machine_QTY", "mysite_qc"."Quantity" as "QC_QTY",\
    # "mysite_painting"."Quantity" as "Painting_QTY", "mysite_painting"."dateEnd" as "Painting_END", \
    # "mysite_qcpainting"."Quantity" as "QCPainting_QTY", "mysite_assembly"."Quantity" as "Assembly_QTY",\
    # "mysite_maker"."name" as "MakerName"\
    # FROM mysite_drawing \
    # LEFT JOIN mysite_document on "drawingNo" ="mysite_document"."drawing_id" \
    # LEFT JOIN mysite_cutting on "drawingNo" ="mysite_cutting"."drawing_id" \
    # LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id" \
    # LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id" \
    # LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" \
    # LEFT JOIN mysite_maker on "drawingNo"="mysite_maker"."drawing_id"')
    return render(request,'drawing/drawingTable.html',{'get_drawing':get_drawing, 'done_qty':done_qty, 'count_drawing':count_drawing , 'job_id':job_id, 'count_drawing_qty':count_drawing_qty, 'get_fileassembly':get_fileassembly, 'get_filemodel':get_filemodel, 'get_fileplan':get_fileplan})

def createDrawing(request,job_id):
    user = request.user
    get_job_id = Job.objects.get(jobNo=job_id)
    if request.method == "POST":
        form = CreateDrawingForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            get_name = data.get('drawingNo')
            get_drawingNo = Drawing.objects.get(drawingNo = get_name)
            File.objects.create(drawing=get_drawingNo,file=f"file/drawing/{get_name}.pdf",user=user)
                                                                                                                                                                                                                                                                                                                              
            
            return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
            
    else:
        form = CreateDrawingForm(initial={'job': get_job_id, 'user': user})
    return render(request, 'drawing/createDrawing.html', {'form': form, 'get_job_id':get_job_id})

def deleteDrawing(request,job_id,drawing_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if str(request.user.username) == str(get_drawing_id.user) or request.user.is_superuser or request.user.is_staff:
        try:
            get_file_id = File.objects.get(drawing_id = get_drawing_id)
            get_file_id.delete()
            get_drawing_id.delete()
        except:
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


def flowSearch(request):
    data = Drawing.objects.all()
    return render(request, 'flowsearch.html',{'drawing':data})



def workflow(request,drawing_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)

    try:
        get_document_id = Document.objects.get(drawing=get_drawing_id)
    except Document.DoesNotExist:
        get_document_id = None

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
    
    return render(request,'workflow.html',{'get_document_id':get_document_id,'get_drawing_id':get_drawing_id, 'get_maker_id':get_maker_id, 'get_machine_id':get_machine_id, 'get_painting_id':get_painting_id})
 







def createDocument(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_document_id = Document.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = CreateDocumentForm(request.POST)
            if form.is_valid():
                get_document = form.save()
                if get_document.skipAssembly == True:
                    Assembly.objects.filter(drawing_id=get_drawing_id).delete()
                    Assembly.objects.create(drawing_id=get_drawing_id)
                    Assembly.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
                else:
                    try:
                        get_assembly = Assembly.objects.filter(drawing_id=get_drawing_id)
                        get_assembly.delete()
                    except:
                        pass
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = CreateDocumentForm(initial={'drawing':get_drawing_id, 'user':user})
        return render(request, 'document/createDocument.html', { 'form':form, 'get_drawing_id':get_drawing_id})

def deleteDocument(request,drawing_id,document_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.user.is_superuser:
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
        get_document = form.save()
        if get_document.skipAssembly == True:
            Assembly.objects.filter(drawing_id=get_drawing_id).delete()
            Assembly.objects.create(drawing_id=get_drawing_id)
            Assembly.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
        else:
            try:
                get_assembly = Assembly.objects.filter(drawing_id=get_drawing_id)
                get_assembly.delete()
            except:
                pass
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editDocument',{'get_drawing_id':get_drawing_id, 'get_document_id':get_document_id})









def createMaker(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_maker_id = Maker.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = CreateMakerForm(request.POST)
            if form.is_valid():
                get_maker = form.save()
                if get_maker.name != 'OPAutotech':
                    Cutting.objects.filter(drawing_id=get_drawing_id).delete()
                    Machine.objects.filter(drawing_id=get_drawing_id).delete()
                    Cutting.objects.create(drawing_id=get_drawing_id)
                    Machine.objects.create(drawing_id=get_drawing_id)
                    Cutting.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
                    Machine.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
                
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

def deleteMaker(request,drawing_id,maker_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.user.is_superuser:
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
        get_maker = form.save()
        if get_maker.name != 'OPAutotech':
            Cutting.objects.filter(drawing_id=get_drawing_id).delete()
            Machine.objects.filter(drawing_id=get_drawing_id).delete()
            Cutting.objects.create(drawing_id=get_drawing_id)
            Machine.objects.create(drawing_id=get_drawing_id)
            Cutting.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
            Machine.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
        else:
            Cutting.objects.filter(drawing_id=get_drawing_id).delete()
            Machine.objects.filter(drawing_id=get_drawing_id).delete()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editMaker',{'get_drawing_id':get_drawing_id, 'get_maker_id':get_maker_id})









def createCutting(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_cutting_id = Cutting.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = CreateCuttingForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = CreateCuttingForm(initial={'drawing':get_drawing_id, 'user':user})
        return render(request, 'cutting/createcutting.html', { 'form':form, 'get_drawing_id':get_drawing_id })

def deleteCutting(request,drawing_id,cutting_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.user.is_superuser:
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
    try:
        get_machine_id = Machine.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
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
    if request.user.is_superuser:
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
    try:
        get_qc_id = Qc.objects.get(machine_id=get_machine_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
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
    if request.user.is_superuser:
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
    try:
        get_painting_id = Painting.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
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
    if request.user.is_superuser:
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
    try:
        get_qcpainting_id = QcPainting.objects.get(painting_id=get_painting_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
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
    if request.user.is_superuser:
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








def createAssembly(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_assembly_id = Assembly.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form  = CreateAssemblyForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = CreateAssemblyForm(initial={'drawing':get_drawing_id, 'user':user})
        return render(request, 'assembly/createassembly.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deleteAssembly(request,drawing_id,assembly_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.user.is_superuser:
        get_assembly_id = Assembly.objects.get(id=assembly_id)
        get_assembly_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))

def editAssembly(request,drawing_id,assembly_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_assembly_id = Assembly.objects.get(id=assembly_id)
    return render(request, 'assembly/editassembly.html',{'get_drawing_id':get_drawing_id, 'get_assembly_id':get_assembly_id})


def updateAssembly(request,drawing_id,assembly_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_assembly_id = get_object_or_404(Assembly, pk=assembly_id)
    form = UpdateAssemblyForm(request.POST, instance=get_assembly_id)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    return redirect('/editAssembly',{'get_drawing_id':get_drawing_id, 'get_assembly_id':get_assembly_id})







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
    if request.user.is_superuser:
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



def uploadFile(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    try:
        get_file_id = File.objects.get(drawing=get_drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = UploadFileForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'uploadfile.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deleteFile(request,drawing_id,file_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    if request.user.is_superuser:
        get_file_id = File.objects.get(id=file_id)
        get_file_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))


def uploadAssemblyFile(request,job_id):
    user = request.user
    get_job_id = Job.objects.get(jobNo=job_id)
    try:
        get_assemblyfile_id = AssemblyFile.objects.get(job=get_job_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_job_id,)))
    except:
        if request.method == "POST":
            form = UploadAssemblyFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
        else:
            form = UploadAssemblyFileForm(initial={'job':get_job_id, 'user':user})
    return render(request, 'uploadassemblyfile.html', {'form':form, 'get_job_id':get_job_id})

def deleteAssemblyFile(request,job_id,assemblyfile_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    if request.user.is_superuser:
        get_assemblyfile_id = AssemblyFile.objects.get(job=job_id)
        get_assemblyfile_id.delete()
    return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))

def uploadPlanFile(request,job_id):
    user = request.user
    get_job_id = Job.objects.get(jobNo=job_id)
    try:
        get_planfile_id = PlanFile.objects.get(job=get_job_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_job_id,)))
    except:
        if request.method == "POST":
            form = UploadPlanFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))
        else:
            form = UploadPlanFileForm(initial={'job':get_job_id, 'user':user})
    return render(request, 'uploadplanfile.html', {'form':form, 'get_job_id':get_job_id})

def deletePlanFile(request,job_id,planfile_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    if request.user.is_superuser:
        get_planfile_id = PlanFile.objects.get(job=job_id)
        get_planfile_id.delete()
    return HttpResponseRedirect(reverse('mysite:drawingTable', args=(get_job_id,)))


def uploadModelFile(request,job_id):
    user = request.user
    get_job_id = Job.objects.get(jobNo=job_id)
    get_modelfile_id = 0
    try:
        get_modelfile_id = ModelFile.objects.get(job=get_job_id)
        form = UploadModelFileForm(instance=get_modelfile_id)
        if request.method == "POST" and form.is_valid:
            form = UploadModelFileForm(request.POST,request.FILES,instance=get_modelfile_id)
            form.save()
    except:
        if request.method == "POST":
            form = UploadModelFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:uploadModelFile', args=(get_job_id,)))
        else:
            form = UploadModelFileForm(initial={'job':get_job_id, 'user':user})
    return render(request, 'uploadModelFile.html', {'form':form, 'get_job_id':get_job_id, 'get_modelfile_id':get_modelfile_id})

def deletepdfFile(request,job_id,modelfile_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_modelfile_id = ModelFile.objects.get(id=modelfile_id)
    if request.user.is_superuser:
        if not get_modelfile_id.fileEdrawing:
            get_modelfile_id.delete()
        else:
            os.remove(get_modelfile_id.filepdf.path)
            ModelFile.objects.filter(job=job_id).update(filepdf=None)
    return HttpResponseRedirect(reverse('mysite:uploadModelFile', args=(get_job_id,)))

def deleteEdrawingFile(request,job_id,modelfile_id):
    get_job_id = Job.objects.get(jobNo=job_id)
    get_modelfile_id = ModelFile.objects.get(id=modelfile_id)
    if request.user.is_superuser:
        if not get_modelfile_id.filepdf:
            get_modelfile_id.delete()
        else:
            os.remove(get_modelfile_id.fileEdrawing.path)
            ModelFile.objects.filter(job=job_id).update(fileEdrawing=None)
    return HttpResponseRedirect(reverse('mysite:uploadModelFile', args=(get_job_id,)))


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})