"""mypracto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from doctor.views import Doctor_cls
from patient.views import Patient_cls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

doc_obj = Doctor_cls()
pat_obj= Patient_cls()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',doc_obj.login_selection_page),
    path('newwelcome/',doc_obj.login_select_page),
    path('newwelcome/newwelcome',doc_obj.login_select_page),
    path('',include("doctor.urls")),
    path('',include("patient.urls")),   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
else:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)