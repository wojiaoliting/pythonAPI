# -*- coding: utf-8 -*-
__author__ = 'LX'

from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['userId'] = self.user.id

        # Add extra responses here
        # data['username'] = self.user.username
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        self.user.last_login = datetime.now()
        self.user.save()
        return data


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

