from django import forms
from .models import AppointmentForm


class AppointmentModelForm(forms.ModelForm):
    class Meta:
        model = AppointmentForm
        fields = '__all__'

