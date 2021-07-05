from django.urls import path
from mysite import views
# from .views import DrawingDetail
app_name = 'mysite'


urlpatterns = [
    path('', views.homepage),

    path('createJob',views.createJob),
    path('jobTable',views.jobTable, name= 'jobTable'),
    path('jobTable/edit/<str:job_id>',views.editJob),
    path('jobTable/update/<str:job_id>',views.updateJob),
    path('jobTable/delete/<str:job_id>',views.deleteJob),



    path('allDrawing',views.allDrawing, name= 'allDrawing'),  
    path('createDrawing/<str:job_id>',views.createDrawing, name= 'createDrawing'),  
    path('drawingTable/<str:job_id>',views.drawingTable, name= 'drawingTable'),
    path('drawingTable/<str:job_id>/edit/<str:drawing_id>',views.editDrawing),
    path('drawingTable/<str:job_id>/update/<str:drawing_id>',views.updateDrawing),
    path('drawingTable/<str:job_id>/delete/<str:drawing_id>',views.deleteDrawing),


    path('workflow/<str:drawing_no>',views.workflow, name= 'workflow'),

]