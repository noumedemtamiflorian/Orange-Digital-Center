from django.shortcuts import render
from django.http import  Http404
from .models import  Profile
# Create your views here.
def detail(request,username):

    profile = Profile.objects.filter(user_name=username)
    if not profile.exists():
        raise Http404
    profile_obj = profile.first()
    context = {
        "username" : username
    }
    return render(request,"profiles/detail.html")