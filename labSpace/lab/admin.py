from django.contrib import admin
from .models import Aaya

# Register your models here.

@admin.register(Aaya)
class AayaAdmin(admin.ModelAdmin):
	list_display = ('id','aya','is_used')