from django.urls import path
from mysite import views
# from .views import DrawingDetail
app_name = 'mysite'


urlpatterns = [
    path('', views.homepage),

    path('jobTable',views.jobTable, name= 'jobTable'),
    path('createJob',views.createJob),
    path('jobTable/edit/<str:job_id>',views.editJob),
    path('jobTable/update/<str:job_id>',views.updateJob),
    path('jobTable/delete/<str:job_id>',views.deleteJob),



    path('allDrawing',views.allDrawing, name= 'allDrawing'),

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
]