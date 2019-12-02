from django.conf.urls import url

from MdfMine import views

urlpatterns = [
    url(r'^login/',views.login),
    url(r'^getcode/',views.get_code),
    url(r'^getdata/',views.getdata),
    url(r'^mdfdt/',views.mdfdt,name='mdfdt'),
    url(r'^upload/',views.upload,name='upload'),

    ]

