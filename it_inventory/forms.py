from django import forms
from .models import  Insumo,User,WorkStation

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class WorkStationForm(forms.ModelForm):
    class Meta:
        model = WorkStation
        fields = '__all__'
        widgets = {
            'date_received': forms.DateInput(attrs={'type': 'date'}),
        }

class QueryInsumoForm(forms.Form):
    nombre=forms.CharField(max_length=100,required=False,label='Buscar por nombre')