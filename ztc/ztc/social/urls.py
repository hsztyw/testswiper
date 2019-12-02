from django.conf.urls import url

from social import views

urlpatterns = [
    url(r'^recommed/',views.recommed),
    url(r'^addlike',views.addlike)
]