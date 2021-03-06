# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-30 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('oid', models.IntegerField()),
                ('ltype', models.CharField(choices=[('like', '喜欢'), ('suplike', '超级喜欢'), ('dislike', '不喜欢')], max_length=10)),
                ('ltime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelaFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('oid', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='relafriend',
            unique_together=set([('uid', 'oid')]),
        ),
    ]
