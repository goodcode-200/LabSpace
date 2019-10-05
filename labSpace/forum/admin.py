from django.contrib import admin
from .models import Title

# Register your models here.
@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
	list_display = ('id','title')