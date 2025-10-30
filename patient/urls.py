from django.urls import path
from patient.views import Patient_cls
from django.conf.urls.static import static
from django.conf import settings
from .import views
pat_obj = Patient_cls()

urlpatterns = [
   path('patient-register',pat_obj.addRegis_page,name='patient-register'),
   path('register-patient', pat_obj.insert_patient, name='register-patient'),
   path("profile-patient",pat_obj.pat_profile_page,name='profile-patient'),
   path("patient_login",pat_obj.patient_login,name="patient_login"),
   path("patient-login",pat_obj.patient_login_page,name='patient-login'),
   path("patient-login/patient-login",pat_obj.patient_login_page,name='patient-login'),
   path("logout-patient",pat_obj.logout,name="logout-patient"),
   path('schedule-appointment', pat_obj.schedule_appointment, name='schedule_appointment'),
   path('send_otp_patient/', views.sendOTPPatient, name='send_otp'),
   path('reset_password_patient', views.resetPasswordPatient, name='reset_password'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
else:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)