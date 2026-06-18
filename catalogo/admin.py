# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)
