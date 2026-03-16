from django.shortcuts import render, redirect
# render: genera una respuesta HTML usando un template
# redirect: devuelve una redirección HTTP a otra URL
from it_inventory.forms import InsumoForm, UserForm, WorkStationForm, QueryInsumoForm
from it_inventory.models import Insumo
# Importamos los formularios para usarlos en las vistas
# Importamos el modelo Insumo para poder consultar la base de datos

# Create your views here.
def home(request):
    """
    Home page view.

    Receives an HTTP request and returns the home template.
    """
    return render(request, 'it_inventory/home.html') # render() genera un HttpResponse con el HTML del template

def add_insumo(request):
    """
    View used to create a new Insumo in the database.

    Handles both:
    - displaying the form (GET request)
    - processing the submitted form (POST request)
    """
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InsumoForm()
    return render(request, 'it_inventory/form_generic.html', {
            'form': form,
            'titulo': 'Add Insumo'
        })

def add_user(request):
    """
    View used to create a new users in the database.

    Handles both:
    - displaying the form (GET request)
    - processing the submitted form (POST request)
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'it_inventory/form_generic.html', {
        'form': form,
        'titulo': 'Add User'
    })

def add_ws(request):
    """
    View used to create a new work stations in the database.

    Handles both:
    - displaying the form (GET request)
    - processing the submitted form (POST request)
    """
    if request.method == 'POST':
        form = WorkStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WorkStationForm()
    return render(request, 'it_inventory/form_generic.html', {
        'form': form,
        'titulo': 'Add WorkStation'
    })

def query_insumo(request):
    """
    View used to search Insumo objects by name.
    """
    query = request.GET.get('nombre','')
    results = []
    if query:
        results = Insumo.objects.filter(name__icontains=query)

    form = QueryInsumoForm()

    return render(request, 'it_inventory/query.html', {
        'form': form,
        'results': results,
        'query': query,
    })