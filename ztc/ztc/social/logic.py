import datetime

from MdfMine.models import Profile, User
from social.models import OptLike, RelaFriend


def recomuser(uid):
    mine,_ = Profile.objects.get_or_create(id = uid)
    user = User.objects.filter(
        sex = mine.sex,
        loc_city= mine.loc_city,
        birth_year__gte = datetime.date.today().year - mine.max_dating_age,
        birth_day__lte= datetime.date.today().year - mine.min_dating_age,
    )[0:50]

    return user

def adlk(uid,oid):
    ctlike = OptLike.objects.create(uid=uid,oid=oid,ltype='喜欢')
    print(oid)
    if ctlike.check_like(uid,oid):
        RelaFriend.objects.create(uid=uid,oid=oid)
        return True
    return False

