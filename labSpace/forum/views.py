from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from user.utils import authenticate
from user.models import User
from .models import Title,Tag
from itertools import chain
from .utils import get_pre_obj,get_next_obj

# Create your views here.
def index(request):
    context = {}
    titles = Title.objects.all()
    context["titles"] = titles
    return render(request,'forum/forum_list.html',context)

@authenticate
def publish(request):
    if request.method == "POST":
        try:
            title = request.POST.get("title").strip()
            content = request.POST.get("content").strip()
            nickname = request.session.get("nickname")
            user = User.objects.get(nickname=nickname)
            title_obj = Title(title=title,content=content,author=user)
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
        except:
            return HttpResponseBadRequest("Bad Request")
    else:
        context = {}
        nickname = request.session.get("nickname")
        context["user"] = nickname
        return render(request,'forum/publish.html',context)

@authenticate  #登录核验
def search(request): #模糊查询(涵盖主题的title和标签)
    if request.method == "POST":
        key = request.POST.get('key').strip()
        context = {}
        titles = Title.objects.filter(title__icontains=key)
        tags = Tag.objects.filter(tag_name__icontains=key)
        for tag_obj in tags:
            titles = chain(titles,tag_obj.title_set.all())
        titles = list(set(titles))  #去重
        context["titles"] = titles
        context["key"] = key
        return render(request,'forum/search_list.html',context)
    else:
        return HttpResponseRedirect("/forum/")

def tagInfo(request,tag_pk):
    context = {}
    tag = Tag.objects.get(pk=tag_pk)
    titles = tag.title_set.all()
    context["titles"] = titles
    context["tag"] = tag.tag_name
    return render(request,'forum/taginfo.html',context)

def detail(request,title_pk):
    context = {}
    context["title"] = Title.objects.get(pk=title_pk)
    context["pre"] = get_pre_obj(int(title_pk))
    context["next"] = get_next_obj(int(title_pk))
    return render(request,'forum/detail.html',context)