# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-28 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MdfMine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='loc_city',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('郑州', '郑州'), ('西安', '西安'), ('成都', '成都'), ('沈阳', '沈阳')], max_length=10, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='loc_provice',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('郑州', '郑州'), ('西安', '西安'), ('成都', '成都'), ('沈阳', '沈阳')], max_length=10, verbose_name='省'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='ico', max_length=128, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='loc_city',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('郑州', '郑州'), ('西安', '西安'), ('成都', '成都'), ('沈阳', '沈阳')], max_length=10, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='user',
            name='loc_provice',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('郑州', '郑州'), ('西安', '西安'), ('成都', '成都'), ('沈阳', '沈阳')], max_length=10, verbose_name='省'),
        ),
    ]
