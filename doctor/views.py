import json,random
from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Doctor,Specialty
from patient.models import Appointment
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.hashers import check_password
# Create your views here.
otp_storage = {} 
class Doctor_cls:
    @csrf_exempt
    def login_selection_page(self,request):
         return render(request, 'welcome.html')
    def login_select_page(self,request):
        return render(request, 'newwelcom.html')
    def register_doctor(self,request):
        print("==== Inside register_doctor ====")
        if request.POST.get("name") is not None and request.POST.get("name") !="" and request.POST.get("email") is not None and request.POST.get("email") !="" and request.POST.get("qualification") is not None and request.POST.get("qualification") !="" and request.POST.get("specialty") is not None and request.POST.get("specialty") !="" and request.POST.get("year_of_experience") is not None and request.POST.get("year_of_experience") !="" and request.POST.get("phone_no") is not None and request.POST.get("phone_no") !="" and request.POST.get("gender") is not None and request.POST.get("gender") !="" and request.POST.get("fee") is not None and request.POST.get("fee") !="" and request.POST.get("time") is not None and request.POST.get("time") !="" and request.POST.get("password") is not None and request.POST.get("password") !="":
            print("DEBUG:", request.POST.dict())
            createDoctor = Doctor.objects.create(
                name = request.POST["name"] ,
                email = request.POST["email"],
                qualification = request.POST["qualification"],
                specialty = Specialty.objects.get(id=request.POST["specialty"]),
                year_of_experience = request.POST["year_of_experience"],
                phone_no = request.POST["phone_no"],
                gender = request.POST["gender"],
                fee=request.POST["fee"],
                time=request.POST["time"],
                password=request.POST["password"],
            )
            if createDoctor:
                return JsonResponse({"message": "successfully inserted", 
                                     "redirect": "/doctor-login"})
            else:
                return JsonResponse({"message":"something went wrong"})
        else:
            return JsonResponse({"message":"one or more field is empty"})
        
        
    def addRegis_page(self,request):
        fetchAllSpecialties=Specialty.objects.all()
        return render(request, 'doctor_registration.html',{"specialties":fetchAllSpecialties})
    
    def doc_profile_page(self,request):
        if request.method =="GET":
            print("Session Doctor ID:", request.session.get("doctor_id"))
            if request.session.get("doctor_id") is not None and request.session.get("doctor_id") !="":
             try:
                    #fetchDermatologist=Doctor.objects.select_related("specialty").filter(specialty__specialty_name="Dermatologist")
                    fetchDoc=Doctor.objects.select_related("specialty").get(id=request.session["doctor_id"])
                    appointments = Appointment.objects.filter(doctor_id=fetchDoc).select_related("patient_id")
                    print("Appointments:", appointments)
                    all_docs={"name":fetchDoc.name,"qualification":fetchDoc.qualification,"specialty":fetchDoc.specialty.specialty_name,"email":fetchDoc.email, "time":fetchDoc.time,"fee":fetchDoc.fee}
                    print("---------------------",all_docs)
                    
                    return render(request,"dr_profile.html",{'doc_details':all_docs,'appointments':appointments,})
             except Doctor.DoesNotExist:
                 return render(request,"404.html")   
            else:
                return HttpResponseRedirect("newwelcom.html/")
        else:
            return render(request,"404.html") 
    
    
    def doctor_login_page(self,request):
        return render(request,"login.html")
    
    def doctor_login(self,request):
        if request.method == "POST":
            if request.POST.get("email") is not None and request.POST.get("email") != "" and request.POST.get("password") is not None and request.POST.get("password") != "":
                email = request.POST["email"]
                password = request.POST["password"]
                try:
                    fetchDoc = Doctor.objects.get(email=email)
                    if password == fetchDoc.password:
                        request.session["doctor_id"] = fetchDoc.id
                        messages.success(request, "Login successful")
                        return HttpResponseRedirect('/profile-doctor')
                    else:
                        messages.error(request, "Invalid credentials")
                        return JsonResponse({"message":"Invalid credentials"})
                except Doctor.DoesNotExist:
                    return JsonResponse({"message":"Doctor id does not exist"})
            else:
                return JsonResponse({"message":"One or more field is empty"})
        else:
            return JsonResponse({"message":"Only Post is allowed"})
        
    def logout(self,request):
        request.session.pop("doctor_id",None)
        return HttpResponseRedirect("newwelcome/")

@csrf_exempt
def send_otp(request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                email = data.get("email")
                if not email:
                  return JsonResponse({ "error": "Email is required" })
                if not Doctor.objects.filter(email=email).exists():
                    return JsonResponse({"error": "Doctor with this email does not exist"}, status=404)
                otp = str(random.randint(100000, 999999))
                otp_storage[email] = otp
                send_mail(
                    "Password Reset OTP",
                    f"Your OTP for password reset is: {otp}",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return JsonResponse({"message": "OTP sent successfully."})
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
        return JsonResponse({"error": "Invalid request method"}, status=405)
@csrf_exempt
def reset_password(request):
        if request.method == 'POST':
            email = request.POST.get("email")
            otp = request.POST.get("otp")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if otp_storage.get(email) != otp:
                return HttpResponse("Invalid OTP", status=400)

            if new_password != confirm_password:
                return HttpResponse("Passwords do not match", status=400)

            try:
                doctor = Doctor.objects.get(email=email)
                doctor.password = new_password
                doctor.save()
                del otp_storage[email]
                return HttpResponse("Password reset successful.")
            except Doctor.DoesNotExist:
                return HttpResponse("Doctor not found", status=404)

        return HttpResponse("Invalid request method.", status=405)
def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Scheduled"
    appointment.save()
    return redirect('profile-doctor')

def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Rejected"
    appointment.save()
    return redirect('profile-doctor')
@csrf_exempt      
def get_doctors(request):
        if request.method == "POST":
            data = json.loads(request.body)
            specialty_id = data.get('specialty_id')
            doctors = Doctor.objects.filter(specialty_id=specialty_id)
            doctor_list=[{'id':d.id, 'name':d.name} for d in doctors]
            return JsonResponse({'doctors': doctor_list})
        return JsonResponse({'error': 'Invalid request method'}, status=400)