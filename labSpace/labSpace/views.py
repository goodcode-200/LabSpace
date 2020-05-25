from django.shortcuts import render
from user.utils import get_nickname

def index(request):
    context = {}
    context["nickname"] = get_nickname(request)
    return render(request, 'index.html',context)