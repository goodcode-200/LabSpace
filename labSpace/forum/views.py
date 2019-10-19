from django.shortcuts import render
#from django.core.urlresolvers import reverse  #使用这个反向解析会循环引用！！！
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import Title,Tag
from user.models import UserProfile
from itertools import chain

def home(request):
    context = {}
    titles = Title.objects.all()
    context["titles"] = titles
    return render(request,'forum/forum_list.html',context)

@login_required(login_url="/user/account/")  #登录核验
def search(request): #模糊查询(涵盖主题的title和标签)
    if request.method == "POST":
        key = request.POST.get('key')
        context = {}
        titles = Title.objects.filter(title__icontains=key)
        tags = Tag.objects.filter(tag_name__icontains=key)
        for tag_obj in tags:
            titles = chain(titles,tag_obj.title_set.all())
        titles = list(set(titles))  #去重
        context["titles"] = titles
        return render(request,'forum/search_list.html',context)
    else:
        return HttpResponseRedirect("/forum/")

@login_required(login_url="/user/account/")  #登录核验
def publish(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        userprofile = UserProfile.objects.get(user=request.user)
        title_obj = Title(title=title,content=content,userprofile=userprofile)
        title_obj.save()

        tags = request.POST.get("tags").strip(" /").split("/")
        tag_obj_list = [] #初始化标签对象容器
        for tag in tags:
            tag = tag.strip()
            if tag:
                tag_obj = Tag.objects.filter(tag_name = tag)
                if tag_obj:
                    tag_obj = tag_obj[0]
                else:
                    tag_obj = Tag(tag_name=tag)
                    tag_obj.save()
                tag_obj_list.append(tag_obj)
            else:
                continue
        title_obj.tags.add(*tag_obj_list)
        return HttpResponse("<h1>发布成功！</h1>")
    else:
        context = {}
        user = request.user
        return render(request,'forum/publish.html',context)
