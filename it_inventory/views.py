from django.shortcuts import render, redirect
# render: genera una respuesta HTML usando un template
# redirect: devuelve una redirección HTTP a otra URL
from it_inventory.forms import InsumoForm, UserForm, WorkStationForm, QueryInsumoForm, QueryUserForm, \
    QueryWorkStationForm
from it_inventory.models import Insumo, User, WorkStation


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

    """
    this thing called context down there is what it is send 
    to the template and it is used there to get the values put here
    """
    return render(request, 'it_inventory/query.html', {
        'form': form,
        'results': results,
        'query': query,
        'subject': "Insumnos",
        'action_url': 'query_insumo',
    })

def query_user(request):
    query = request.GET.get('name','') # the request.get.get is a check if the user actually typed something, then saves what he typed into query

    results = []
    if query: # if the request actually got something then it ask the databese, if the name field contain the query, then it saves the filter array into results
        results = User.objects.filter(name__icontains=query)
    form = QueryUserForm()

    return render(request, 'it_inventory/query.html', {
        'form': form,
        'results': results,
        'query': query,
        'subject': "Users",
        'action_url': 'query_user',
    })
def query_ws(request):
    query = request.GET.get('ws_number','')
    results = []
    if query:
        results = WorkStation.objects.filter(ws_number__icontains=query)
    form = QueryWorkStationForm()

    return render(request, 'it_inventory/query.html', {
        'form': form,
        'results': results,
        'query': query,
        'subject': "Work Stations",
        'action_url': 'query_ws',
    })