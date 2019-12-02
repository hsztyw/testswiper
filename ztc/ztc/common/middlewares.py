
from django.utils.deprecation import MiddlewareMixin

from common import statude
from lib.http import rend_json


class AuthMiddleware(MiddlewareMixin):


    path_white_list = [
        '/user/login/',
        '/api/user/submit_vcode',
    ]

    def process_request(self, request):
        if request.path not in self.path_white_list:
            uid = request.session.get('uid')
            if not uid:
                return rend_json('登录失败',statude.LOGIN_FAIL)
            else:
                request.id = uid
