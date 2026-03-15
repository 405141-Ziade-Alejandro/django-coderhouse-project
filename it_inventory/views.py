from django.shortcuts import render, redirect

from it_inventory.forms import InsumoForm, UserForm, WorkStationForm, QueryInsumoForm
from it_inventory.models import insumo


# Create your views here.
def home(request):
    return render(request, 'it_inventory/home.html')

def add_insumo(request):
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
    query = request.GET.get('nombre','')
    results = []
    if query:
        results = insumo.objects.filter(name__icontains=query)

    form = QueryInsumoForm()

    return render(request, 'it_inventory/query.html', {
        'form': form,
        'results': results,
        'query': query,
    })