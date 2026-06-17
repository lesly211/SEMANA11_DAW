import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda.settings")
django.setup()

from catalogo.models import Producto

Producto.objects.all().delete()

Producto.objects.create(
    nombre="smart tv samsung 55 pulgadas",
    descripcion="televisor led ultra hd 4k con funciones smart y control por voz.",
    precio=1899.00,
    stock=12
)

Producto.objects.create(
    nombre="laptop asus rog zephyrus",
    descripcion="computadora portatil gamer con procesador amd ryzen 9 y tarjeta rtx 4070.",
    precio=7499.00,
    stock=5
)

Producto.objects.create(
    nombre="auriculares sony wh-1000xm4",
    descripcion="auriculares inalambricos con cancelacion de ruido lider en la industria y 30 horas de bateria.",
    precio=1199.00,
    stock=3
)

Producto.objects.create(
    nombre="teclado mecanico keychron k2",
    descripcion="teclado mecanico inalambrico compacto al 75% con switches brown e iluminacion rgb.",
    precio=450.00,
    stock=15
)

Producto.objects.create(
    nombre="mouse inalambrico logitech mx master 3",
    descripcion="mouse ergonomico premium disenado para programadores y disenadores con rueda magspeed.",
    precio=399.00,
    stock=20
)

print("productos insertados exitosamente:")
for p in Producto.objects.all():
    print(f"- {p.nombre} (Stock: {p.stock})")
