from django.http import HttpRequest,HttpResponse,HttpResponseBadRequest
from .models import Aaya,Lab


def check_regi_aya(view):
    def wrapper(request:HttpRequest):
        try:
            aya = request.POST.get("space_id").strip()
            Aaya.objects.get(aya=aya,is_used=False)
            ret = view(request) # 调用传入的view
            return ret
        except:
            return HttpResponse("<h1>空间码错误或访问方式异常！<h1/>")
    return wrapper

# 这里的这个只有space参数
def check_enter_permission(view):
    def wrapper(request:HttpRequest,space):
        try:
            lab = Lab.objects.get(address=space)
            nickname = request.session.get("nickname")
            lab_list = lab.members.all().filter(nickname=nickname)
            if lab_list:
                ret = view(request, space)
            else:
                return HttpResponse("您不是该实验室的成员，您无权限进入或进行该实验室的相关操作！")
            return ret
        except:
            return HttpResponseBadRequest("Bad Request")
    return wrapper

# 这里的这个只有space参数
def check_enter_permission_space(view):
    def wrapper(request:HttpRequest,space,index):
        try:
            lab = Lab.objects.get(address=space)
            nickname = request.session.get("nickname")
            lab_list = lab.members.all().filter(nickname=nickname)
            if lab_list or lab.is_public == True:
                ret = view(request, space, index)
            else:
                return HttpResponse("您不是该私有实验室的成员，您无权限进入")
            return ret
        except:
            return HttpResponseBadRequest("Bad Request")
    return wrapper

