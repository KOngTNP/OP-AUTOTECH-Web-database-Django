"""OPAutotech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import urls, views 
from accounts import views as v

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
import mysite

from django.contrib import admin

admin.site.site_header = 'OPAUTOTECH'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Adminsitration' # default: "Django site admin"
urlpatterns = [
    path('', include('mysite.urls', namespace='mysite')),
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'mysite.views.custom_page_not_found_view'
handler500 = 'mysite.views.custom_error_view'
handler403 = 'mysite.views.custom_permission_denied_view'
handler400 = 'mysite.views.custom_bad_request_view'