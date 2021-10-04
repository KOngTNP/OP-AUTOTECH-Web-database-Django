from mysite.models import Painting
from django.urls import path
from mysite import views
# from .views import DrawingDetail
app_name = 'mysite'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reportTable',views.reportTable, name= 'reportTable'),

    
    path('jobTable',views.jobTable, name= 'jobTable'),
    path('jobReport/<str:job_id>', views.jobReport, name='jobReport'),
    path('createJob',views.createJob),
    path('jobTable/edit/<str:job_id>',views.editJob),
    path('jobTable/update/<str:job_id>',views.updateJob),
    path('jobTable/delete/<str:job_id>',views.deleteJob),



    path('drawingTable/<str:job_id>',views.drawingTable, name='drawingTable'),
    path('createDrawing/<str:job_id>',views.createDrawing, name= 'createDrawing'),  
    path('drawingTable/<str:job_id>/edit/<str:drawing_id>',views.editDrawing),
    path('drawingTable/<str:job_id>/update/<str:drawing_id>',views.updateDrawing),
    path('drawingTable/<str:job_id>/delete/<str:drawing_id>',views.deleteDrawing),



    path('workflow/<str:drawing_id>',views.workflow, name= 'workflow'),

    path('createDocument/<str:drawing_id>',views.createDocument, name= 'createDocument'),
    path('workflow/<str:drawing_id>/edit/document/<int:document_id>',views.editDocument),
    path('workflow/<str:drawing_id>/update/document/<int:document_id>',views.updateDocument),
    path('workflow/<str:drawing_id>/delete/document/<int:document_id>',views.deleteDocument),


    path('createMaker/<str:drawing_id>',views.createMaker, name='createMaker'),
    path('workflow/<str:drawing_id>/edit/maker/<int:maker_id>',views.editMaker),
    path('workflow/<str:drawing_id>/update/maker/<int:maker_id>',views.updateMaker),
    path('workflow/<str:drawing_id>/delete/maker/<int:maker_id>',views.deleteMaker),


    path('createCutting/<str:drawing_id>',views.createCutting, name='createCutting'),
    path('workflow/<str:drawing_id>/edit/cutting/<int:cutting_id>',views.editCutting),
    path('workflow/<str:drawing_id>/update/cutting/<int:cutting_id>',views.updateCutting),
    path('workflow/<str:drawing_id>/delete/cutting/<int:cutting_id>',views.deleteCutting),



    path('createMachine/<str:drawing_id>',views.createMachine, name='createMachine'),
    path('workflow/<str:drawing_id>/edit/machine/<int:machine_id>',views.editMachine),
    path('workflow/<str:drawing_id>/update/machine/<int:machine_id>',views.updateMachine),
    path('workflow/<str:drawing_id>/delete/machine/<int:machine_id>',views.deleteMachine),



    path('createQc/<str:drawing_id>',views.createQc, name='createQc'),
    path('workflow/<str:drawing_id>/edit/qc/<int:qc_id>',views.editQc),
    path('workflow/<str:drawing_id>/update/qc/<int:qc_id>',views.updateQc),
    path('workflow/<str:drawing_id>/delete/qc/<int:qc_id>',views.deleteQc),


    path('createPainting/<str:drawing_id>',views.createPainting, name='createPainting'),
    path('workflow/<str:drawing_id>/end/painting/<int:painting_id>',views.endPainting),
    path('workflow/<str:drawing_id>/edit/painting/<int:painting_id>',views.editPainting),
    path('workflow/<str:drawing_id>/update/painting/<int:painting_id>',views.updatePainting),
    path('workflow/<str:drawing_id>/delete/painting/<int:painting_id>',views.deletePainting),


    path('createQcPainting/<str:drawing_id>',views.createQcPainting, name='createQcPainting'),
    path('workflow/<str:drawing_id>/edit/qcpainting/<int:qcpainting_id>',views.editQcPainting),
    path('workflow/<str:drawing_id>/update/qcpainting/<int:qcpainting_id>',views.updateQcPainting),
    path('workflow/<str:drawing_id>/delete/qcpainting/<int:qcpainting_id>',views.deleteQcPainting),


    path('createAssembly/<str:drawing_id>',views.createAssembly, name='createAssembly'),
    path('workflow/<str:drawing_id>/edit/assembly/<int:assembly_id>',views.editAssembly),
    path('workflow/<str:drawing_id>/update/assembly/<int:assembly_id>',views.updateAssembly),
    path('workflow/<str:drawing_id>/delete/assembly/<int:assembly_id>',views.deleteAssembly),

    path('createRevise/<str:drawing_id>',views.createRevise, name='createRevise'),
    path('workflow/<str:drawing_id>/edit/revise/<int:revise_id>',views.editRevise),
    path('workflow/<str:drawing_id>/update/revise/<int:revise_id>',views.updateRevise),
    path('workflow/<str:drawing_id>/delete/revise/<int:revise_id>',views.deleteRevise),

    path('uploadFile/<str:drawing_id>',views.uploadFile, name='uploadFile'),
    path('workflow/<str:drawing_id>/delete/file/<int:file_id>',views.deleteFile),

    path('workflow',views.flowSearch, name='flowSearch')
]