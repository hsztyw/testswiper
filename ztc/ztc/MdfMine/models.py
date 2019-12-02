from django.db import models

# Create your models here.
from ztc.api_cof import NationalCities


class User(models.Model):
    nc = NationalCities()
    provice_city = nc.choice(nc.prct)
    provices = (("北京", "北京"),
        ("上海", "上海"),
        ("深圳", "深圳"),
        ("郑州", "郑州"),
        ("西安", "西安"),
        ("成都", "成都"),
        ("沈阳", "沈阳"),)
    citys = (        ("北京", "北京"),
        ("上海", "上海"),
        ("深圳", "深圳"),
        ("郑州", "郑州"),
        ("西安", "西安"),
        ("成都", "成都"),
        ("沈阳", "沈阳"),
                     )
    sexs = (
        ('男','mail'),
        ('女','famail')
    )
    phonenum = models.CharField(max_length=12,verbose_name='手机号')
    nickname = models.CharField(max_length=32,verbose_name='昵称')
    sex = models.CharField(default='男',choices=sexs,max_length=4,verbose_name='性别')
    birth_year = models.IntegerField(default=2000,verbose_name='年')
    birth_month = models.IntegerField(default=1,verbose_name='月')
    birth_day = models.IntegerField(default=1,verbose_name='日')
    avatar = models.CharField(default='ico',max_length=128,verbose_name='头像')
    loc_provice = models.CharField(max_length=10,choices=provices,verbose_name='省')
    loc_city = models.CharField(max_length=10,choices=citys,verbose_name='城市')

    class Mate:
        db_table = 'user'

    def to_dict(self):
        return {
            'id':self.id,
        'phonenum':self.phonenum,
        'nickname':self.nickname,
        'sex':self.sex,
        'birth_year':self.birth_year,
        'birth_month':self.birth_month,
        'birth_day':self.birth_day,
        'avatar':self.avatar,
        'loc_provice':self.loc_provice,
        'loc_city':self.loc_city,
        }


class Profile(models.Model):
    loc_provice = models.CharField(max_length=10,choices=User.provices,verbose_name='省')
    loc_city = models.CharField(max_length=10,choices=User.citys,verbose_name='城市')
    min_distance=models.IntegerField(default=1,verbose_name='最⼩查找范围')
    max_distance=models.IntegerField(default=10,verbose_name='最⼤查找范围')
    min_dating_age=models.IntegerField(default=18,verbose_name='最⼩交友年龄')
    max_dating_age=models.IntegerField(default=50,verbose_name='最⼤交友年龄')
    sex = models.CharField(default='男',choices=User.sexs,max_length=4,verbose_name='性别')
    vibration=models.BooleanField(default=True,verbose_name='开启震动')
    only_matche=models.BooleanField(default=False,verbose_name='不让为匹配的⼈看我的相册')
    auto_play=models.BooleanField(default=True,verbose_name='⾃动播放视频')

    class Meta():
        db_table = 'profile'

    def to_dict(self):
        return {
        'id':self.id,
        'loc_provice':self.loc_provice,
        'loc_city':self.loc_city,
        'min_distance':self.min_distance,
        'max_distance':self.max_distance,
        'min_dating_age':self.min_dating_age,
        'max_dating_age':self.max_dating_age,
        'sex':self.sex,
        'vibration':self.vibration,
        'only_matche':self.only_matche,
        'auto_play':self.auto_play,
        }