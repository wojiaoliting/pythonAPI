# -*- coding: utf-8 -*-
__author__ = 'LX'


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = UserProfile
        fields = ("user", "nickname", "gender", "mobile", "birthday", "id", "icon", "created", "updated")
        read_only_fields = ['id']

        # fields=('__all__')


class UserSerializer(serializers.ModelSerializer):
    """
        用户列表序列化类
    """
    profile_of = UserProfileSerializer(required=False)
    # article_from = ArticleSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'last_login', 'profile_of')
        # fields = ('__all__')
        read_only_fields = ['last_login', 'profile_of']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # validated_data['profile_of'] = null
        # 接受前端传过来的用户名和密码
        user = User(**validated_data)
        # 通过字典方式调用
        user.set_password(validated_data['password'])
        # user.created = datetime.now()
        # validated_data['profile_of'] = self.context.get("profile_of")
        # user_profile = UserProfile.objects.create(**validated_data)
        # 保存到内存中
        user.save()
        return user
