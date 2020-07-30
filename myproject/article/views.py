# -*- coding: utf-8 -*-
__author__ = 'LX'

from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from user.customPagination import UserPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Article.objects.all().order_by('-created')
    serializer_class = ArticleSerializer
    # ordering=('-id',)
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'summary')
    # permission_classes = [permissions.IsAuthenticated]
    # pagination_class =
    # def list(self, request):
    #     list= Article.objects.all()
    #     # print(list)
    #     data=ArticleSerializer(list)
    #     print(data)
    #     return Response('data')


    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    def destroy(self, request, pk=None):
        instance = Article.objects.get(id=pk)
        instance.title_icon.delete(save=False)
        instance.delete()
        json=('statu','true')
        return Response(json,status.HTTP_200_OK)
