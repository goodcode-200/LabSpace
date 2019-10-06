from django.shortcuts import render
#from django.core.urlresolvers import reverse  #使用这个反向解析会循环引用！！！
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Title

def home(request):
	context = {}
	titles = Title.objects.all()
	context["titles"] = titles
	return render(request,'forum/forum_list.html',context)

@login_required(login_url="/user/account/")  #登录核验
def search(request): #模糊查询
	if request.method == "POST":
		key = request.POST.get('key')
		context = {}
		titles = Title.objects.filter(title__icontains=key)
		context["titles"] = titles
		return render(request,'forum/search_list.html',context)
	else:
		return HttpResponseRedirect("/forum/")