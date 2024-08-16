from django.shortcuts import render, redirect
from .forms import songForm
import sweetify

class cancion():
    def __init__(self, name, descripcion):
        self.name = name
        self.descripcion = descripcion
c1 = cancion("Take My Breath - TheWeeknd", "La mejor cancion de TheWeeknd")
canciones = [c1]


# Create your views here.
def index(request):
    names = []
    for i in canciones:
        names.append(i.name)
    if len(canciones) == 0:
        context = {
        "names":names,
        "vacio": True
        }
    else:
        context = {
        "names":names,
        "vacio": False
        }
    return render(request, 'listas/contenido1.html',context)

def descripcion(request,name):
    context = {
        "name": None,
        "descripcion": "No se ha encontrado la canción"
    }
    for i in canciones:
        if i.name == name:
            context["name"] = i.name
            context["descripcion"] = i.descripcion
            sweetify.toast(request, 'Accediendo a descripcion', icon="success", timer=3000)
    if not context["name"]:
        sweetify.toast(request, 'Cancion no encontrada', icon="error", timer=3000)

    return render(request, "listas/contenido2.html", context)

def agregar(request):
    if request.method == 'POST':
        form = songForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data["name"]
           descripcion  = form.cleaned_data["descripcion"]
           canciones.append(cancion(name,descripcion))
           sweetify.toast(request, 'Cancion agregada correctamente', icon="success", timer=3000)
           return redirect("index")
    else:
        return render(request, "listas/agregar.html", { "form": songForm()})
    
def eliminar(request,name):
    if request.method == 'POST':
        for i in canciones:
            if i.name == name:
                canciones.remove(i)
    sweetify.toast(request, 'Cancion eliminada correctamente', icon="warning", timer=3000)
    return redirect("index")

    
        
            
            

