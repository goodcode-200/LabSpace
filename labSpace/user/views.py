from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
from .utils import *

# Create your views here.
def account(request):
	return render(request,'user/account.html')

def register(request):
	context={}
	if request.method == 'POST':
		# 是否重名
		name = request.POST.get('username').strip()
		user = User.objects.filter(username=name)
		if user:
			return HttpResponse("注册失败,该用户名已经被使用。")
		# 是否重邮箱
		email = request.POST.get('email')
		user = User.objects.filter(email = email)
		if user:
			return HttpResponse("注册失败,此邮箱已经被注册。")
		# 获取密码
		password = request.POST.get('password')
		# 创建用户对象
		user = User.objects.create_user(name, email, password)
		user.save()
		# 获取性别
		sex = request.POST.get('gender')
		sex = "man" if sex=="0" else "woman"
		# 或取用户标识哈希值
		uid = getNewUid()
		# 创建userprofile对象，存储用户基本信息
		userprofile = UserProfile(user=user,sex=sex,uid=uid)
		userprofile.save()
		return HttpResponse("注册成功")
	else:
		return HttpResponseRedirect("/user/account")

def userLogin(request):
	if request.method == "POST":
		name = request.POST.get('Name').strip()
		password = request.POST.get('password')
		user = authenticate(username=name, password=password)
		if user:
			if user.is_active:
				#request.session["username"] = user.username
				login(request,user)
				return HttpResponse("登录成功")
			else:
				return HttpResponse("您的用户已经被限制,请联系工作人员")
		else:
			return HttpResponse("登录失败，用户名或密码错误！")
	else:
		return HttpResponseRedirect("/user/account")