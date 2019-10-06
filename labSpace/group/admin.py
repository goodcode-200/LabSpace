from django.contrib import admin
from .models import LabGroup

# Register your models here.
@admin.register(LabGroup)
class LabGroupAdmin(admin.ModelAdmin):
	list_display = ('id','group')