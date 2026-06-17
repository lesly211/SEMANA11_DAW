from django.test import TestCase
from django.urls import reverse
from .models import Producto

class ProductoModelAndViewsTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="producto de prueba",
            descripcion="descripcion de prueba",
            precio=99.99,
            stock=10
        )

    def test_modelo_producto(self):
        self.assertEqual(str(self.producto), "producto de prueba")

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/home.html")

    def test_catalogo_view(self):
        response = self.client.get(reverse("catalogo"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/catalogo.html")
        self.assertContains(response, "Producto De Prueba")
