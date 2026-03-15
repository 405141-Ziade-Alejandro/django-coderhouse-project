from django import forms
from .models import  insumo,user,work_station

class InsumoForm(forms.ModelForm):
    class Meta:
        model = insumo
        fields = '__all__'
class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
class WorkStationForm(forms.ModelForm):
    class Meta:
        model = work_station
        fields = '__all__'
        widgets = {
            'date_received': forms.DateInput(attrs={'type': 'date'}),
        }

class QueryInsumoForm(forms.Form):
    nombre=forms.CharField(max_length=100,required=False,label='Buscar por nombre')