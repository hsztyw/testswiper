from django.shortcuts import render

# Create your views here.
from MdfMine.models import User
from MdfMine.models import  Profile
from lib.http import rend_json
from social.logic import recomuser, adlk


def recommed(request):
    user = recomuser(request.id)
    users = [usr.to_dict()  for usr in user]
    return rend_json(users)

def addlike(request):
    oid = int(request.POST.get('oid'))
    print(oid)
    m = adlk(request.id,oid)
    return rend_json(m)

