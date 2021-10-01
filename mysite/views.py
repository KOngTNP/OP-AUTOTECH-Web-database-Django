from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateJobForm,CreateDrawingForm,UpdateDrawingForm, UpdateJobForm, CreateDocumentForm, UpdateDocumentForm, CreateMakerForm, UpdateMakerForm,CreateCuttingForm, UpdateCuttingForm, CreateMachineForm, UpdateMachineForm, CreateQcForm, UpdateQcForm, CreatePaintingForm ,UpdatePaintingForm, CreateQcPaintingForm ,UpdateQcPaintingForm, CreateAssemblyForm ,UpdateAssemblyForm, CreateReviseForm ,UpdateReviseForm, UploadFileForm
from .models import Assembly, Job, Drawing, Document, Maker, Cutting, Machine, Qc, Painting, QcPainting, User, Revise, File
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.db.models import Q
import datetime


def homepage(request):
    return render(request,'home.html',{'text1':'wellcome to homepage','text2':'this is test homepage'})





def reportTable(request):
    get_user_id = User.objects.all
    select_all_report = Drawing.objects.raw(
        'SELECT "job_id" as "Job_number", "projectName" as "Project_name",\
        "drawingNo", "mysite_drawing"."Quantity" as "Drawing_QTY", "mysite_drawing"."datePublish" as "Drawing_date",\
        "mysite_document"."Quantity" as "Document_QTY", "mysite_document"."user_id" as "Document_user", "mysite_document"."datePublish" as "Document_date",\
        "mysite_maker"."name" as "Maker_name",\
        "mysite_cutting"."Quantity" as "Cutting_QTY", "mysite_cutting"."user_id" as "Cutting_user", "mysite_cutting"."datePublish" as "Cutting_date",\
        "mysite_machine"."Quantity" as "Machine_QTY", "mysite_machine"."user_id" as "Machine_user", "mysite_machine"."machine" as "Machine_number", "mysite_machine"."datePublish" as "Machine_date",\
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

    document_day_report = Document.objects.raw("""SELECT * FROM mysite_document WHERE "mysite_document"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_document"."datePublish";""")
    document_week_report = Document.objects.raw("""SELECT *, to_char("datePublish", 'day') as "day" FROM mysite_document WHERE "mysite_document"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_document"."datePublish";""")
    document_month_report = Document.objects.raw("""SELECT * FROM mysite_document WHERE "mysite_document"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_document"."datePublish";""")
    
    # maker_day_report = Maker.objects.raw('SELECT * FROM mysite_maker where "mysite_maker"."datePublish" > now() - interval "1 day";')
    # maker_week_report = Maker.objects.raw('SELECT *, to_char("datePublish", "day") FROM mysite_maker WHERE "mysite_maker"."datePublish" >= date_trunc("week", CURRENT_DATE);')
    # maker_month_report = Maker.objects.raw('SELECT * FROM mysite_maker WHERE "mysite_maker"."datePublish" >= date_trunc("month", CURRENT_DATE);')

    cutting_day_report = Cutting.objects.raw("""SELECT * FROM mysite_cutting WHERE "mysite_cutting"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_cutting"."datePublish";""")
    cutting_week_report = Cutting.objects.raw("""SELECT *, to_char("datePublish", 'day') as "day" FROM mysite_cutting WHERE "mysite_cutting"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_cutting"."datePublish";""")
    cutting_month_report = Cutting.objects.raw("""SELECT * FROM mysite_cutting WHERE "mysite_cutting"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_cutting"."datePublish";""")
    
    machine_day_report = Machine.objects.raw("""SELECT * FROM mysite_machine WHERE "mysite_machine"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_machine"."datePublish";""")
    machine_week_report = Machine.objects.raw("""SELECT *, to_char("datePublish", 'day') as day FROM mysite_machine WHERE "mysite_machine"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_machine"."datePublish";""")
    machine_month_report = Machine.objects.raw("""SELECT * FROM mysite_machine WHERE "mysite_machine"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_machine"."datePublish";""")

    qc_day_report = Qc.objects.raw("""SELECT "mysite_qc"."id", "mysite_machine"."drawing_id", "mysite_qc"."Quantity", "mysite_qc"."datePublish", "mysite_qc"."dateUpdate", "mysite_qc"."user_id" FROM mysite_qc LEFT JOIN mysite_machine on "mysite_machine"."id" ="mysite_qc"."machine_id" WHERE "mysite_qc"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_qc"."datePublish";""")
    qc_week_report = Qc.objects.raw("""SELECT "mysite_qc"."id", "mysite_machine"."drawing_id", "mysite_qc"."Quantity", "mysite_qc"."datePublish", "mysite_qc"."dateUpdate", "mysite_qc"."user_id", to_char("mysite_qc"."datePublish", 'day') as "day" FROM mysite_qc LEFT JOIN mysite_machine on "mysite_machine"."id" ="mysite_qc"."machine_id" WHERE "mysite_qc"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_qc"."datePublish";""")
    qc_month_report = Qc.objects.raw("""SELECT "mysite_qc"."id", "mysite_machine"."drawing_id", "mysite_qc"."Quantity", "mysite_qc"."datePublish", "mysite_qc"."dateUpdate", "mysite_qc"."user_id" FROM mysite_qc LEFT JOIN mysite_machine on "mysite_machine"."id" ="mysite_qc"."machine_id" WHERE "mysite_qc"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_qc"."datePublish";""")

    painting_day_report = Painting.objects.raw("""SELECT * FROM mysite_painting WHERE "mysite_painting"."dateEnd" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_painting"."dateEnd";""")
    painting_week_report = Painting.objects.raw("""SELECT *, to_char("dateEnd", 'day') as "day" FROM mysite_painting WHERE "mysite_painting"."dateEnd" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_painting"."dateEnd";""")
    painting_month_report = Painting.objects.raw("""SELECT * FROM mysite_painting WHERE "mysite_painting"."dateEnd" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_painting"."dateEnd";""")

    qcpainting_day_report = QcPainting.objects.raw("""SELECT "mysite_qcpainting"."id", "mysite_painting"."drawing_id", "mysite_qcpainting"."Quantity", "mysite_qcpainting"."datePublish", "mysite_qcpainting"."dateUpdate", "mysite_qcpainting"."user_id" FROM mysite_qcpainting LEFT JOIN mysite_painting on "mysite_painting"."id" ="mysite_qcpainting"."painting_id" WHERE "mysite_qcpainting"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_qcpainting"."datePublish";""")
    qcpainting_week_report = QcPainting.objects.raw("""SELECT "mysite_qcpainting"."id", "mysite_painting"."drawing_id", "mysite_qcpainting"."Quantity", "mysite_qcpainting"."datePublish", "mysite_qcpainting"."dateUpdate", "mysite_qcpainting"."user_id", to_char("mysite_qcpainting"."datePublish", 'day') as "day" FROM mysite_qcpainting LEFT JOIN mysite_painting on "mysite_painting"."id" ="mysite_qcpainting"."painting_id" WHERE "mysite_qcpainting"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_qcpainting"."datePublish";""")
    qcpainting_month_report = QcPainting.objects.raw("""SELECT "mysite_qcpainting"."id", "mysite_painting"."drawing_id", "mysite_qcpainting"."Quantity", "mysite_qcpainting"."datePublish", "mysite_qcpainting"."dateUpdate", "mysite_qcpainting"."user_id" FROM mysite_qcpainting LEFT JOIN mysite_painting on "mysite_painting"."id" ="mysite_qcpainting"."painting_id" WHERE "mysite_qcpainting"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_qcpainting"."datePublish";""")

    assembly_day_report = Assembly.objects.raw("""SELECT * FROM mysite_assembly WHERE "mysite_assembly"."datePublish" >= date_trunc('day', CURRENT_DATE) ORDER BY "mysite_assembly"."datePublish";""")
    assembly_week_report = Assembly.objects.raw("""SELECT *, to_char("datePublish", 'day') as "day" FROM mysite_assembly WHERE "mysite_assembly"."datePublish" >= date_trunc('week', CURRENT_DATE) ORDER BY "mysite_assembly"."datePublish";""")
    assembly_month_report = Assembly.objects.raw("""SELECT * FROM mysite_assembly WHERE "mysite_assembly"."datePublish" >= date_trunc('month', CURRENT_DATE) ORDER BY "mysite_assembly"."datePublish";""")
    return render(request,'reportTable.html',
    {
        'get_user_id':get_user_id,
        'select_all_report':select_all_report,
        
        'document_day_report':document_day_report, 'document_week_report':document_week_report, 'document_month_report':document_month_report,
        # 'maker_day_report':maker_day_report, 'maker_week_report':maker_week_report, 'maker_month_report':maker_month_report,
        'cutting_day_report':cutting_day_report, 'cutting_week_report':cutting_week_report, 'cutting_month_report':cutting_month_report,
        'machine_day_report':machine_day_report, 'machine_week_report':machine_week_report, 'machine_month_report':machine_month_report,
        'qc_day_report':qc_day_report, 'qc_week_report':qc_week_report, 'qc_month_report':qc_month_report,
        'painting_day_report':painting_day_report, 'painting_week_report':painting_week_report, 'painting_month_report':painting_month_report,
        'qcpainting_day_report':qcpainting_day_report, 'qcpainting_week_report':qcpainting_week_report, 'qcpainting_month_report':qcpainting_month_report,
        'assembly_day_report':assembly_day_report, 'assembly_week_report':assembly_week_report, 'assembly_month_report':assembly_month_report
        
    
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
    all_qty = Job.objects.raw('SELECT "mysite_job"."jobNo", sum("mysite_drawing"."Quantity") as "QTY" FROM mysite_drawing , mysite_job WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" GROUP BY "mysite_job"."jobNo"')
    done_qty = Job.objects.raw('SELECT "mysite_job"."jobNo" as "jobNo", sum("mysite_assembly"."Quantity") as "Assembly_QTY" FROM mysite_job, mysite_drawing LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" WHERE "mysite_job"."jobNo" = "mysite_drawing"."job_id" GROUP BY "mysite_job"."jobNo"')
    return render(request,'job/jobTable.html',{'jobs':data, 'all_qty':all_qty, 'done_qty':done_qty})

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
                percent = 0
            if all.Document_QTY != None:
                perDocument = percent*all.Document_QTY
            else:
                perDocument = 0
            if all.Cutting_QTY != None:
                perCutting = percent*all.Cutting_QTY
            else:
                perCutting = 0
            if all.Machine_QTY != None:
                perMachine = percent*all.Machine_QTY
            else:
                perMachine = 0
            if all.Qc_QTY != None:
                perQc = percent*all.Qc_QTY
            else: 
                perQc = 0
            if all.Painting_QTY != None:
                perPainting = percent*all.Painting_QTY
            else:
                perPainting = 0
            if all.PaintingQc_QTY != None:
                perPaintingQc = percent*all.PaintingQc_QTY
            else:
                perPaintingQc = 0
            if all.Assembly_QTY != None:
                perAssembly = percent*all.Assembly_QTY
            else:
                perAssembly = 0

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
    done_qty = Drawing.objects.raw(
    'SELECT "mysite_drawing"."drawingNo" as "drawingNo", "mysite_document"."Quantity" as "Document_QTY", \
    "mysite_cutting"."Quantity" as "Cutting_QTY", "mysite_machine"."Quantity" as "Machine_QTY", "mysite_qc"."Quantity" as "QC_QTY",\
    "mysite_painting"."Quantity" as "Painting_QTY", "mysite_painting"."dateEnd" as "Painting_END", \
    "mysite_qcpainting"."Quantity" as "QCPainting_QTY", "mysite_assembly"."Quantity" as "Assembly_QTY",\
    "mysite_maker"."name" as "MakerName"\
    FROM mysite_drawing \
    LEFT JOIN mysite_document on "drawingNo" ="mysite_document"."drawing_id" \
    LEFT JOIN mysite_cutting on "drawingNo" ="mysite_cutting"."drawing_id" \
    LEFT JOIN mysite_machine LEFT JOIN mysite_qc on "mysite_machine"."id" ="mysite_qc"."machine_id"  on  "drawingNo" ="mysite_machine"."drawing_id" \
    LEFT JOIN mysite_painting LEFT JOIN mysite_qcpainting on  "mysite_painting"."id" ="mysite_qcpainting"."painting_id"  on  "drawingNo" ="mysite_painting"."drawing_id" \
    LEFT JOIN mysite_assembly on "drawingNo" ="mysite_assembly"."drawing_id" \
    LEFT JOIN mysite_maker on "drawingNo"="mysite_maker"."drawing_id"')
    return render(request,'drawing/drawingTable.html',{'get_job_id':get_job_id, "done_qty":done_qty})

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


def flowSearch(request):
    data = Drawing.objects.all()
    return render(request, 'flowSearch.html',{'drawing':data})



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
    text = ""
    try:
        get_document_id = Document.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = CreateDocumentForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = CreateDocumentForm(initial={'drawing':get_drawing_id, 'user':user})
        return render(request, 'document/createDocument.html', { 'form':form, 'get_drawing_id':get_drawing_id ,'text':text})

def createDocumentandAssembly(request,drawing_id):
    user = request.user
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    text = "(Skip Assembly)"
    try:
        get_document_id = Document.objects.get(drawing_id=drawing_id)
        return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    except:
        if request.method == "POST":
            form = CreateDocumentForm(request.POST)
            assemblyForm  = CreateAssemblyForm(request.POST)
            if form.is_valid():
                form.save()
                assemblyForm.save()
                return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
        else:
            form = CreateDocumentForm(initial={'drawing':get_drawing_id, 'user':user})
            assemblyForm = CreateAssemblyForm(initial={'drawing':get_drawing_id, 'user':user})

        return render(request, 'document/createDocument.html', { 'form':form, 'assemblyForm':assemblyForm, 'get_drawing_id':get_drawing_id, 'text':text })

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
                    Machine.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity, machine = 'othercompany')
                
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
                Cutting.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity)
                Machine.objects.filter(drawing_id=get_drawing_id).update(user = User.objects.get(username='othercompany'), Quantity = get_drawing_id.Quantity, machine = 'othercompany')
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
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
    else:
        form = UploadFileForm(initial={'drawing':get_drawing_id, 'user':user})
    return render(request, 'uploadfile.html', {'form':form, 'get_drawing_id':get_drawing_id})

def deleteFile(requset,drawing_id,file_id):
    get_drawing_id = Drawing.objects.get(drawingNo=drawing_id)
    get_file_id = File.objects.get(id=file_id)
    get_file_id.delete()
    return HttpResponseRedirect(reverse('mysite:workflow', args=(get_drawing_id,)))
