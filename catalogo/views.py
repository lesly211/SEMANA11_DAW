from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

def home(request):
    visitas = request.session.get("visitas", 0) + 1
    request.session["visitas"] = visitas
    context = {
        "titulo": "inicio de la tienda",
        "descripcion": "bienvenido a nuestra tienda virtual construida con django 5.",
        "visitas": visitas
    }
    return render(request, "catalogo/home.html", context)

class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo/catalogo.html"
    context_object_name = "productos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_seccion"] = "catalogo completo de productos"
        return context
