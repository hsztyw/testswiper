from django.db import models

# Create your models here.
class OptLike(models.Model):
    likelist=(
        ('like','喜欢'),
        ('suplike','超级喜欢'),
        ('dislike','不喜欢'),
    )
    uid = models.IntegerField()
    oid = models.IntegerField()
    ltype = models.CharField(max_length=10,choices=likelist)
    ltime = models.DateTimeField(auto_now_add=True)

    @classmethod
    def check_like(cls,uid,oid):
        print(uid,oid)
        return cls.objects.filter(uid = uid,oid=oid).exists()



class RelaFriend(models.Model):
    uid = models.IntegerField()
    oid = models.IntegerField()

    class Meta:
        unique_together = [['uid','oid']]
