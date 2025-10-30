from django import forms
from .models import Appointment
from doctor.models import Specialty, Doctor
import re

class AppointmentForm(forms.ModelForm):
    specialist = forms.ModelChoiceField(label="Specialty",
        queryset=Specialty.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    doctor_id = forms.ModelChoiceField(label="Select Doctor",
        queryset=Doctor.objects.all(), 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}))
    issue = forms.CharField(max_length=255, 
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter issue'}))
    appointment_date = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    

    class Meta:
        model = Appointment
        fields = ['specialist', 'doctor_id', 'issue', 'appointment_date']
    def clean_issue(self):
        issue = self.cleaned_data.get('issue')
        if not re.match(r'^[a-zA-Z0-9\s]+$', issue):
            raise forms.ValidationError("Issue must contain only alphanumeric characters and spaces.")
        return issue
    def clean(self):
        cleaned_data = super().clean()
        specialist = cleaned_data.get('specialist')
        doctor_id = cleaned_data.get('doctor_id')

        if specialist and doctor_id and doctor_id.specialty!= specialist:
            raise forms.ValidationError("The selected doctor does not match the selected specialty.")
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        specialty_id = kwargs.pop('specialty_id', None)
        super().__init__(*args, **kwargs)
        if specialty_id:
            self.fields['doctor_id'].queryset = Doctor.objects.filter(specialty_id=specialty_id)
        else:
            self.fields['doctor_id'].queryset = Doctor.objects.none() 

    