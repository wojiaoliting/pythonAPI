# -*- coding: utf-8 -*-
__author__ = 'LX'

from rest_framework import serializers
from .uploadWebsitImg import BaseToImg
from .models import Article
from django.conf import settings
from user.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    # 正向查找
    author = serializers.CharField(source='user.username', required=False, read_only=True)
    # get_user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'summary', 'body', 'title_icon', 'created', 'author')
        # read_only_fields = ['id', "created"]
        # fields=('__all__')

    def create(self, validated_data):
        body = validated_data['body']
        imgList = BaseToImg(html=body).startReptiles()
        validated_data['body'] = imgList
        article = Article(**validated_data)
        article.save()
        return article
        # fields=('__all__')

    def update(self, instance, validated_data):
        imgList = BaseToImg(html=validated_data['body'], oldHtml=instance.body,type='put').startReptiles()
        validated_data['body'] = imgList
        # print(validated_data['body'])  如果碰到unicode码输出会报错
        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.body = validated_data.get('body', instance.body)
        if 'title_icon' in validated_data.keys():
            instance.title_icon.delete(save=False)
        instance.title_icon = validated_data.get('title_icon', instance.title_icon)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance



