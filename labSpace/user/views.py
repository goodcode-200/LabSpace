from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import User
from datetime import timedelta


# Create your views here.
def reg(request):
    return render(request,'user/reg.html')

def login(request):
    return render(request, 'user/login2.html')

def deal_reg(request):
    if request.method == "POST":
        nickname = request.POST.get('nickname').strip()
        # 避免重复
        user_list = User.objects.filter(nickname=nickname)
        if(user_list):
            return HttpResponseBadRequest("Bad Request")
        name = request.POST.get('name').strip()
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = User()
        user.nickname = nickname
        user.name = name
        user.email = email
        user.password = password
        user.save()
        return HttpResponse("注册成功！")
    else:
        return HttpResponseRedirect("/")

def deal_login(request):
    if request.method == "POST":
        nickname = request.POST.get("form-username")
        password = request.POST.get("form-password")
        user_list = User.objects.filter(nickname=nickname,password=password)
        if(user_list):
            is_keep = request.POST.get("is_keep")
            user = user_list[0]
            request.session["nickname"] = user.nickname
            if is_keep:
                request.session.set_expiry(30*24*60*60)
            else:
                request.session.set_expiry(0)
            return HttpResponse("登录成功!<a href='/'>跳转首页</a>")
        return HttpResponse("登录失败")
    else:
        return HttpResponseRedirect("/")

def user_logout(request):
    request.session.delete()
    return HttpResponseRedirect("/")

def test(request):
    return HttpResponse(request.session.get("nickname",""))

def get_nickname(request,nickname):
    try:
        nickname = nickname.strip()
        user_list = User.objects.filter(nickname=nickname)
        if user_list:
            res = JsonResponse({
                'user': {
                    'is_exist':True
                }
            })
        else:
            res = JsonResponse({
                'user': {
                    'is_exist':False
                }
            })
        return res
    except:
        return HttpResponseBadRequest("Bad Request")

