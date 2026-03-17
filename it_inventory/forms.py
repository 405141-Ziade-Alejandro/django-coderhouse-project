from django import forms
from .models import  Insumo,User,WorkStation

class InsumoForm(forms.ModelForm):
    """
    Form automatically generated from the Insumo model.

    ModelForm allows Django to create HTML form fields based on
    the model fields definition.
    """
    class Meta:
        model = Insumo
        fields = '__all__'
class UserForm(forms.ModelForm):
    """
    Form used to create or edit User objects.
    """
    class Meta:
        model = User
        fields = '__all__'
class WorkStationForm(forms.ModelForm):
    """
    Form used to create or edit WorkStation objects.
    """
    class Meta:
        model = WorkStation
        fields = '__all__'
        widgets = {
            'date_received': forms.DateInput(attrs={'type': 'date'}),
        }

class QueryInsumoForm(forms.Form):
    """
    Simple form used to search Insumo objects by name.

    Unlike ModelForm, this form is not tied to a database model.
    It only collects input data for a query.
    """
    nombre=forms.CharField(max_length=100,required=False,label='Buscar por nombre')

class QueryUserForm(forms.Form):
    name=forms.CharField(max_length=100,required=False,label='Buscar por nombre')

class QueryWorkStationForm(forms.Form):
    ws_number=forms.CharField(max_length=100,required=False,label='Buscar por WS Etiqueta')