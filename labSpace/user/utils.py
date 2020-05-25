from django.http import HttpResponse,HttpResponseRedirect

# 用户登录与否判断的装饰器,用户未登录就返回到登陆页面让用户自己登录
def authenticate(view):
    def wrapper(request:HttpResponse,*args):
        nickname = request.session.get("nickname", "")
        if(nickname):
            if(args):
                ret = view(request,args[0]) # 调用视图函数
            else:
                ret = view(request)
            # 特别注意的是view调用的时候，里面也有返回异常
            return ret
        else:
            return HttpResponseRedirect("/user/login")
    return wrapper

def authenticate_space(view):
    def wrapper(request:HttpResponse,space,index):
        nickname = request.session.get("nickname", "")
        if(nickname):
            ret = view(request,space,index) # 调用视图函数
            # 特别注意的是view调用的时候，里面也有返回异常
            return ret
        else:
            return HttpResponseRedirect("/user/login")
    return wrapper

def authenticate_apl(view):
    def wrapper(request:HttpResponse,space):
        nickname = request.session.get("nickname", "")
        if(nickname):
            ret = view(request,space) # 调用视图函数
            # 特别注意的是view调用的时候，里面也有返回异常
            return ret
        else:
            return HttpResponseRedirect("/user/login")
    return wrapper

def get_nickname(request):
    nickname = request.session.get("nickname","")
    return nickname