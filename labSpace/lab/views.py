from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,HttpResponseBadRequest
from .utils import check_regi_aya,check_enter_permission_space,check_enter_permission
from user.utils import authenticate,authenticate_space,authenticate_apl
from .models import Lab,Apply
from blog.models import Blog
from labSpace.settings import PERPAGE_BLOG_NUM
from user.models import User

# Create your views here.
def list_lab(request):
    labs = Lab.objects.all()
    context = {}
    context["labs"] = labs
    return render(request,'lab/lab_list.html',context)

@authenticate # 必须登录
def apply(request):
    return render(request,'lab/apply.html')

@check_regi_aya #空间码必须正确
@authenticate # 必须登录
def apply_deal(request):
    if request.method == "POST":
        try:
            lab_name = request.POST.get("lab_name").strip()
            introduce = request.POST.get("introduce")
            url_id = request.POST.get("url_id").strip()
            is_public = request.POST.get("is_public")

            # url_id 是否已经存在
            lab_list = Lab.objects.filter(address=url_id)
            if lab_list:
                return HttpResponseBadRequest("Bad Request")

            # 正式开始创建开辟空间
            try:
                user_nick = request.session.get("nickname")
            except:
                return HttpResponseBadRequest("Bad Request")
            lab = Lab()
            lab.admin_id = user_nick
            lab.lab_name = lab_name
            lab.introduce = introduce
            lab.address = url_id
            lab.members.add(User.objects.get(nickname=user_nick))
            lab.member_num += 1
            if is_public:
                lab.is_public = True
            else:
                lab.is_public = True
            lab.img = (Lab.objects.all().last().id + 1) % 12 + 1
            lab.save() # 保存了实验室

            return HttpResponse("注册成功！")
        except:
            return HttpResponseBadRequest("Bad Request")
    else:
        return HttpResponseRedirect("/")

def get_address(request,address):
    try:
        add = address.strip()
        lab_list = Lab.objects.filter(address=add)
        if lab_list:
            res = JsonResponse({
                'lab': {
                    'is_exist':True
                }
            })
        else:
            res = JsonResponse({
                'lab': {
                    'is_exist':False
                }
            })
        return res
    except:
        return HttpResponseBadRequest("Bad Request")

@check_enter_permission_space
@authenticate_space
def to_space(request,space,index="1"):
    try:
        lab = Lab.objects.get(address=space)
        context = {}
        context["lab"] = lab
        # 博客的分页展示
        blog_num = Blog.objects.filter(lab=lab).count()
        temp = blog_num // PERPAGE_BLOG_NUM
        total_page = temp if blog_num % PERPAGE_BLOG_NUM == 0 else temp + 1
        current_page = int(index)
        start = (current_page-1)*PERPAGE_BLOG_NUM

        if index == total_page:
            end = blog_num
        else:
            end = start + PERPAGE_BLOG_NUM
        blogs = Blog.objects.filter(lab=lab)[start:end]
        context["blogs"] = blogs
        context["current_page"] = current_page
        context["total_page"] = total_page
        context["pre"] = current_page if current_page == 1 else current_page-1
        context["next"] = current_page if current_page == total_page else current_page+1
        context["page_list"] = map(lambda x:x+1,list(range(total_page)))

        # 请求的展示
        apply_list = Apply.objects.filter(lab=lab)
        context["apply_list"] = apply_list
        return render(request,'lab/space.html',context)
    except:
        return HttpResponseBadRequest("Bad Request")

def change_to_space(request,space):
    return HttpResponseRedirect('/lab/space/' + space + "/1")

@authenticate_apl
def apl(request,space): #申请加入实验室
    try:
        nickname = request.session.get("nickname")
        user = User.objects.get(nickname = nickname)
        lab = Lab.objects.get(address=space)
        user_list = lab.members.all().filter(nickname=nickname)
        if user_list:
            return HttpResponse("你是实验室的成员！")
        else:
            apply_obj = Apply()
            apply_obj.user = user
            apply_obj.lab = lab
            apply_obj.save()
        return HttpResponse("发出请求成功，请等待管理员处理!")
    except:
        return HttpResponseBadRequest("Bad Request")

@authenticate
def apl_deal(request,apl_pk):
    try:
        # 权限判断
        nickname = request.session.get("nickname")
        apl = Apply.objects.get(pk=apl_pk)
        if nickname == apl.lab.admin_id:
            lab = apl.lab
            lab.members.add(User.objects.get(nickname=apl.user.nickname))
            lab.member_num += 1
            lab.save()
            apl.delete()
            return HttpResponseRedirect("/lab/spac/" + lab.address)
        else:
            return HttpResponse("您无对应的权限")
    except:
        return HttpResponseBadRequest("Bad Request")

@authenticate
def apl_del(request,apl_pk):
    try:
        # 权限判断
        nickname = request.session.get("nickname")
        apl = Apply.objects.get(pk=apl_pk)
        if nickname == apl.lab.admin_id:
            lab_address = apl.lab.address
            # 直接删除即可
            apl.delete()
            return HttpResponseRedirect("/lab/spac/" + lab_address)
        else:
            return HttpResponse("您无对应的权限")
    except:
        return HttpResponseBadRequest("Bad Request")