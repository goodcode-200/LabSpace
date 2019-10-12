from django.contrib import admin
from .models import LabGroup,LabDetail,Book,MajorTag,Direction,Honor

# Register your models here.
@admin.register(LabGroup)
class LabGroupAdmin(admin.ModelAdmin):
	list_display = ('id','group','member_num','is_public')

@admin.register(LabDetail)
class LabDetailAdmin(admin.ModelAdmin):
	list_display = ('id','lab')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('id','bookname','author','publisher','lab')

@admin.register(MajorTag)
class MajorTagAdmin(admin.ModelAdmin):
	list_display = ('tag_name',)

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
	list_display = ('id','d_name','leader','lab')

@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
	list_display = ('id','h_name','get_time','lab','direction')