import os
import random

import requests
from django.core.cache import cache

from MdfMine.models import User
from lib.qinu_yun import upload_to_qiniu
from tasks import celery_app
from ztc import api_cof

def random_code(length):
    code =''.join([str(random.randint(0,9)) for x in range(length)])
    return code

def send_code(phonum,code):
    '''
    为了避免高并发的数据安全问题，需要将api-cof的短信验证平台数据变成私有的。因此需要一个copy()
    :param phonum:手机号
    :param code: 验证码
    :return: 返回HttpResponse
    requsets的post请求会返回很多数据，包含
    code 状态码   msg 对应状态码信息(发送成功，发送失败)   count 计费条数   create_data 创建时间
    smsid  短信唯一id   mobile 手机号   uid 请求时透传的uid
    '''
    arges = api_cof.YZX_SMS_ARGS.copy()
    arges['param'] = code
    arges['mobile'] = phonum
    response = requests.post(api_cof.YZX_SMS_API,json=arges)

    if response.status_code == 200 :
        result = response.json()
        print(result['msg'])
        if result['msg'] == 'OK':
            cache.set('phone_code',code,180)
            return True
    return False


#保存图片
def save_img(uid,ico):
    '''将个人形象保存到本地'''
    filename = 'Avatar-%s' % uid
    filepath = './tmp/%s' % ico
    print(filepath)
    with open(filepath, 'wb') as fp:
        for chunk in ico.chunks():
            fp.write(chunk)
    return filename, filepath



@celery_app.task
def ico_upload(uid,ico):
    print(11111111111111111111111)
    filename, filepath = save_img(uid,ico)
    avatar_url = upload_to_qiniu(filename,filepath)
    User.objects.filter(id=uid).update(avatar=avatar_url)
    os.remove(filepath)
# TODO: HELLO

