from django.contrib import admin
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    search_fields = ('username', 'email',)

admin.site.register(Registro, RegistroAdmin)