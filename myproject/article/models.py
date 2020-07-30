# -*- coding: utf-8 -*-
__author__ = 'LX'

from django.db import models
from django.conf import settings
# from django.db.models.signals import pre_delete, post_init, pre_save, post_save
# from django.dispatch.dispatcher import receiver

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='article_from',
                             verbose_name='作者', null=True, )
    title = models.CharField(max_length=70, null=True, verbose_name="标题")
    summary = models.CharField(max_length=200, null=True, blank=True, verbose_name="摘要")
    body = models.TextField(null=True, verbose_name="文本内容")
    views = models.PositiveIntegerField('阅读量', default=0)
    # birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    title_icon = models.ImageField(max_length=200, null=True, blank=True, upload_to='media/uploads/article/%Y/%m/%d/')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    updated = models.DateTimeField('修改时间', auto_now=True)

    # 利用内部Meta类来进行元数据配置项的设置
    class Meta:
        verbose_name = "文章"  # 对象名（单数）
        verbose_name_plural = verbose_name  # 对象名（复数）


    def __str__(self):
        return self.title

# @receiver(pre_delete, sender=Article)
# def article_update():

# @receiver(pre_delete, sender=Article)
# def article_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     print('触发了删除键')
#     instance.title_icon.delete(False)

