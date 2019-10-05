from django.shortcuts import render
from .models import Title

def home(request):
	context = {}
	titles = Title.objects.all()
	context["titles"] = titles
	return render(request,'forum/forum_list.html',context)

def search(request): #模糊查询
	if request.method == "POST":
		key = request.POST.get('key')
		context = {}
		titles = Title.objects.filter(title__contains=key)
		context["titles"] = titles
		return render(request,'forum/search_list.html',context)
	else:
		return

