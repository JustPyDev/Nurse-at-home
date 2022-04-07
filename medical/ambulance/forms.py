from django import forms
from .models import *


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['services']
        fields = "__all__"


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = '__all__'
