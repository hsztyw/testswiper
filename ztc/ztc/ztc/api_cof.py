import json

#省和城市的逻辑
class NationalCities(object):

    def choice(self,prct):
        provice = tuple(prct().keys())
        provices = list()
        for pro in provice:
            provices.append((pro,pro))

        citys_list = sum(list(prct().values()),[])
        citys = list()
        for city in citys_list:
            citys.append((city,city))

        return tuple(provices),tuple(citys)

    @staticmethod
    def prct():
        with open('D:\swiper\mdf\ZTC110\ztc\MdfMine\citys.json', 'r', encoding='utf-8') as fb:
            model = json.load(fb)['provinces']
        provic = dict()
        for citys in model:
            provic[citys['provinceName']] = [citys['citysName'] for citys in citys['citys']]
        return provic


#短信验证
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_ARGS = {
    "sid": "2ff56f07e2d002ab9900777dd4b09edf",
    "token": "d763718424035afc347cbd3bba3813a2",
    "appid": "8235102f41ed4603802b05264c59430e",
    "templateid": "503617",
    "param": None,
    "mobile": None,
}




QN_AK = 'gmlryT5gVxtQRKwpyUcRVmJ0qHdLALD53Pw5zPxx'
QN_SK = 'kpyjhGyO6oKpSpdeW7aOEK0OsP7LpjhRAIvgHewR'
QN_BUCKET_NAME = 'hsztyw'
QN_BASE_URL = 'q1ppsb2up.bkt.clouddn.com'


