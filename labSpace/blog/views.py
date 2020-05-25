from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog
from user.utils import authenticate
from lab.utils import check_enter_permission
from user.models import User
from lab.models import Lab

# Create your views here.
@check_enter_permission
@authenticate
def create_blog(request,space):
    context = {}
    lab = Lab.objects.get(address=space)
    context["lab"] = lab
    return render(request,"lab/create_blog.html",context)

@check_enter_permission
@authenticate
def create_blog_deal(request,space):
    try:
        author_nick = request.session.get("nickname")
        author = User.objects.get(nickname=author_nick)
        title = request.POST.get("title")
        link = request.POST.get("link")
        lab = Lab.objects.get(address=space)
        blog = Blog()
        blog.title = title
        blog.link = link
        blog.author = author
        blog.lab = lab
        blog.save()
        addressRedirect = "/lab/spac/" + space
        return HttpResponseRedirect(addressRedirect)
    except:
        return HttpResponse("提交博客失败")