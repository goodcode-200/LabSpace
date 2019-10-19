from django.contrib import admin
from .models import Title,Tag,Comment

# Register your models here.
@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id','title','show_tags','userprofile','pub_time','comment_num','like_num')
    def show_tags(self,obj):
        return [i.tag_name for i in obj.tags.all()]
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','title','userprofile','pub_time','like_num')
