from django.urls import path
from doctor.views import Doctor_cls, get_doctors, accept_appointment, reject_appointment
from django.conf.urls.static import static
from django.conf import settings
from . import views  

doc_obj = Doctor_cls()

urlpatterns = [
    path('doctor-register', doc_obj.addRegis_page, name='doctor-register'),
    path('register-doctor', doc_obj.register_doctor, name='register-doctor'),
    path("profile-doctor", doc_obj.doc_profile_page, name='profile-doctor'),
    path("doctor_login", doc_obj.doctor_login),
    path("doctor-login", doc_obj.doctor_login_page, name='doctor-login'),
    path("logout-doctor", doc_obj.logout, name="logout-doctor"),
    path('get_doctors', views.get_doctors, name='get_doctors'),
    path('accept-appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    path('reject-appointment/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('reset_password', views.reset_password, name='reset_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
