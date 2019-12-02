import os

from django.core.cache import cache
from django.http import JsonResponse


# Create your views here.
from MdfMine.forms import UserForms, ProfileForms
from MdfMine.logics import send_code, random_code, ico_upload
from MdfMine.models import User, Profile
from common import statude
from lib.http import rend_json
from lib.qinu_yun import upload_to_qiniu
from ztc.api_cof import NationalCities


def get_code(request):
    '''
    1.输入手机号
    2.指定验证码位数
    3.发送验证码
    4.查看短信验证码平台返回值，并根据返回值返回数据
    '''
    phonenum = request.GET.get('phonenum')
    rand_code = random_code(4)
    msg = send_code(phonenum, rand_code)
    if msg:
        return rend_json(data = None,code = statude.YZM_SEND_OK,)
    return rend_json(code=statude.YZM_SEND_DIE, data='发送失败')


def login(request):
    '''
    1.获取手机号
    2.获取验证码
    '''
    phonenum = request.POST.get('phonenum')
    code = request.POST.get('code')
    # print(cache.get('phone_code') == code)
    codes = '1234'
    # if phonenum and cache.get('phone_code') == code:
    if phonenum and codes == code:
        user, _ = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        return rend_json( user.to_dict(),statude.LOGIN_SUCCESS)
    else:
        return rend_json(data=None,code=statude.LOGIN_FAIL)


def getdata(request):
    '''
    1.获取uid
    '''
    uid = request.session.get('uid')
    profile,_ = Profile.objects.get_or_create(id = uid)
    return rend_json(profile.to_dict())


def mdfdt(request):
    #修改个人资料
    user_from = UserForms(request.POST)
    profile_form = ProfileForms(request.POST)

    if not user_from.is_valid():
        return rend_json(user_from.errors,statude.MODIFY_FAIL)
    if not profile_form.is_valid():
        return rend_json(profile_form.errors,statude.MODIFY_FAIL)

    print(user_from.cleaned_data)
    #
    User.objects.filter(id = request.id).update(**user_from.cleaned_data)
    Profile.objects.filter(id=request.id).update(**profile_form.cleaned_data)

    return rend_json(data=None,code=statude.MODIFY_SUCCESS)


def upload(request):
    uid = request.id
    ico = request.FILES.get('ico')
    ico_upload.delay(uid,ico)
    return rend_json('ok')