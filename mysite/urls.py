from django.urls import path
from mysite import views
# from .views import DrawingDetail
app_name = 'mysite'


urlpatterns = [
    path('', views.homepage),
    path('createJob',views.createJob),
    path('jobTable',views.jobTable, name= 'jobTable'),
    path('createDrawing/<str:job_id>',views.createDrawing, name= 'createDrawing'),  
    path('drawingTable/<str:job_id>',views.drawingTable, name= 'drawingTable'),
    # path('delete/<str:job_id>',views.delete),

    path('workflow/<str:drawing_no>',views.workflow, name= 'workflow'),

]