from django import forms

from MdfMine.models import User, Profile


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','sex','birth_year','birth_month','birth_day','loc_provice','loc_city']


class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'