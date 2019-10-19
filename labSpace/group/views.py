from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LabGroup,LabDetail
from django.http import HttpResponse

# Create your views here.
@login_required(login_url="/user/account/")  #登录核验
def home(request):
	context = {}
	labg = LabDetail.objects.all()
	context["groups"] = labg
	return render(request,'group/groups.html',context)

def labDetail(request,pk):
	a = LabGroup.objects.get(pk=pk)
	return HttpResponse(a)

