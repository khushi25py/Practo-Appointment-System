from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Patient ,Appointment,Doctor
from doctor.models import Specialty
from .forms import AppointmentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import json,random
# Create your views here.
otp_storage = {} 
class Patient_cls:
    @csrf_exempt
    def insert_patient(self,request):
        print("==== Inside register_doctor ====")
        if request.POST.get("name") is not None and request.POST.get("name") !="" and request.POST.get("email") is not None and request.POST.get("email") !="" and request.POST.get("phone_number") is not None and request.POST.get("phone_number") !=""  and  request.POST.get("gender") is not None and request.POST.get("gender") !="" and request.POST.get("age") is not None and request.POST.get("age") !="":
            createPatient = Patient.objects.create(
                name=request.POST["name"],
                email=request.POST["email"],
                phone_number=request.POST["phone_number"],
                gender=request.POST["gender"],
                age=request.POST["age"],
                password=request.POST["password"]
            )
            if createPatient:
                return JsonResponse({"message": "successfully inserted",
                                     "redirect":"/patient-login"})
            else:
                return HttpResponse("Failed to create patient")
        else:
            return JsonResponse({"message":"One or more field is missing"})
    def addRegis_page(self,request):
        return render (request,'patient_registration.html')
    
    def pat_profile_page(self,request):
        if request.method == "GET":
            if request.session.get("patient_id") is not None and request.session.get("patient_id") !="":
                try:
                    fetchPat=Patient.objects.get(id=request.session["patient_id"])
                    appointments = Appointment.objects.filter(patient_id=fetchPat).order_by('-id') .select_related("doctor_id") 
                    all_pat={"name":fetchPat.name,"email":fetchPat.email,"phone_number":fetchPat.phone_number,"gender":fetchPat.gender}
                    print("---------------",all_pat)  
                    return render(request,"pat_profile.html",{'pat_details':all_pat,'appointments':appointments,})
                except Patient.DoesNotExist:
                    return render(request,"404.html") 
            else:
                return HttpResponseRedirect("/patient-login")
        else:
            return render(request,"404.html")
        
    def patient_login_page(self,request):
        return render(request,"pat_login.html")
    
    def patient_login(self,request):
        if request.method == "POST":
            if request.POST.get("email") is not None and request.POST.get("email") != "" and request.POST.get("password") is not None and request.POST.get("password") != "":
                email = request.POST["email"]
                password = request.POST["password"]
                try:
                   fetchPat = Patient.objects.get(email=email)
                   if fetchPat.password == password:
                    request.session["patient_id"] = fetchPat.id
                    messages.success(request, "Login successful")
                    return HttpResponseRedirect('/profile-patient')
                   else:
                        messages.error(request, "Invalid credentials")
                        return JsonResponse({"message":"Invalid credentials"})
                except Patient.DoesNotExist:
                    return HttpResponseRedirect("/patient-login",{"message":"Patient id does not exist"})
                   
            else:
                return JsonResponse({"message":"One or more field is empty"})
        else:
            return JsonResponse({"message":"Only Post is allowed"})
    
    def logout(self,request):
        request.session.pop("patient_id",None)
        return HttpResponseRedirect("newwelcome/")  
    def schedule_appointment(self,request):
        form= AppointmentForm()
        if request.method == "POST":
          specialty_id = request.POST.get('specialist')  
          form = AppointmentForm(request.POST, specialty_id=specialty_id)
          if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient_id = Patient.objects.get(id=request.session["patient_id"])
            appointment.status="Applied"
            appointment.save()
            return HttpResponseRedirect("/profile-patient",{"alert":"Appointment Scheduled Successfully"})
          else:
                return JsonResponse({"message": "Form is not valid", "errors": form.errors})
        else:
            form = AppointmentForm()
            return render(request, 'schedule_appointment.html', {'form': form})
@csrf_exempt
def sendOTPPatient(request):
    if request.method == 'POST':
            try:
                data = json.loads(request.body)
                email = data.get("email")
                if not email:
                    return JsonResponse({"message": "Email is required"})
                if not Patient.objects.filter(email=email).exists():
                    return JsonResponse({"message": "Patient does not exist"})
                otp = str(random.randint(100000, 999999))
                otp_storage[email] = otp
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return JsonResponse({"message": "OTP sent successfully"})
            except Patient.DoesNotExist:
                return JsonResponse({"message": "Patient does not exist"})
    return JsonResponse({"message": "Only POST requests are allowed"})
@csrf_exempt
def resetPasswordPatient(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        if otp_storage.get(email) != otp:
                return HttpResponse("Invalid OTP", status=400)

        if new_password != confirm_password:
                return HttpResponse("Passwords do not match", status=400)
        
        if not email or not otp or not new_password:
            return JsonResponse({"message": "All fields are required"})
        
        if email not in otp_storage or otp_storage[email] != otp:
            return JsonResponse({"message": "Invalid OTP"})
        
        try:
            patient = Patient.objects.get(email=email)
            patient.password = new_password
            patient.save()
            del otp_storage[email]  # Clear the OTP after successful reset
            return HttpResponse("Password reset successful.")
        except Patient.DoesNotExist:
            return JsonResponse({"message": "Patient does not exist"})
            
        
    def schedule_appointment(self,request):
        form= AppointmentForm()
        if request.method == "POST":
          specialty_id = request.POST.get('specialist')  
          form = AppointmentForm(request.POST, specialty_id=specialty_id)
          if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient_id = Patient.objects.get(id=request.session["patient_id"])
            appointment.status="Applied"
            appointment.save()
            return HttpResponseRedirect("/profile-patient",{"alert":"Appointment Scheduled Successfully"})
          else:
                return JsonResponse({"message": "Form is not valid", "errors": form.errors})
        else:
            form = AppointmentForm()
            return render(request, 'schedule_appointment.html', {'form': form})
        
        