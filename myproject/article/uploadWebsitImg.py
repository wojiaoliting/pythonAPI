# -*- coding: UTF-8 -*-
import re, os
import uuid
import base64
import time
import datetime
import requests
import socket
from myproject.settings import MEDIA_ROOT, HOST_NAME, BASE_DIR


class BaseToImg():
    def __init__(self, html='', count=0, type='post', oldHtml=''):
        self.type = type
        self.html = html
        self.oldHTml = oldHtml
        self.count = count
        self.article_path = '/media/uploads/article/'

    def changeImgUrl(self, value):
        # print(value.group())
        # print(value.group(2))
        # # print(imgbaseurl)
        # imgbaseurl = value.group(2)
        # if(HOST_NAME in value.group(2)):
        #     regStr=value.group(2).index(HOST_NAME)+len(HOST_NAME)
        #     sqlUrl=value.group(2)[regStr:]
        #     return '<img{}src="{}"{}/>'.format(value.group(1), sqlUrl, value.group(3))
        isurl = re.match(r'http|https', value.group(2))
        isbase64 = re.match(r'data:image/(.*);base64,', value.group(2))
        if (isbase64):
            imgbaseurl = re.sub(r'data:image/(.*);base64,', '', value.group(2))
            extension = re.match(r'data:image/(.*);base64,', value.group(2)).group(1)
            # date = str(int(time.time()))
            date = str(uuid.uuid4()).replace('-', '')+str(int(time.time()))
            img_name = date + '.' + extension
            # img_path = MEDIA_ROOT + self.article_path.format(datetime.datetime.now())
            img_path = MEDIA_ROOT + self.article_path
            if os.path.isfile(img_path+img_name):
                self.count += 1
                img_name = str(int(time.time()))+str(self.count)+'.' + extension
            img = base64.b64decode(imgbaseurl)
            fh = open(img_path + img_name, "wb")
            fh.write(img)
            fh.close()
            return '<img{}src="{}"{}/>'.format(value.group(1), '/media'+self.article_path + img_name, value.group(3))
        elif (isurl):
            data = requests.get(value.group(2)).content
            import imghdr
            extension = '.' + imghdr.what(None, data)
            print(extension)
            if extension not in ['.jpg','.png','.jpeg','.svg','.webp','.gif']:
                return '<img{}src="{}"{}/>'.format(value.group(1), '', value.group(3))
            img_path = MEDIA_ROOT + self.article_path
            # extension = re.search(r'(\.jpeg|\.png|\.jpg|\.svg|\.webp|\.gif)', value.group(2)).group(1)

            # date = str(int(time.time()))
            date = str(uuid.uuid4()).replace('-', '') + str(int(time.time()))
            img_name = date + extension
            if os.path.isfile(img_path+img_name):
                self.count += 1
                img_name = str(int(time.time()))+str(self.count) + extension
            f = open(img_path + img_name, 'wb')
            f.write(data)
            f.close()
            return '<img{}src="{}"{}/>'.format(value.group(1), '/media'+self.article_path + img_name, value.group(3))

    def changeBgUrl(self, value):
        # print(value.group(1))
        # print(value.group(3))
        # # print(imgbaseurl)
        # imgbaseurl = value.group(2)
        # if (HOST_NAME in value.group(1)):
        #     regStr = value.group(1).index(HOST_NAME) + len(HOST_NAME)
        #     sqlUrl = value.group(1)[regStr:]
        #     return "background-image: url('{}')".format(sqlUrl)
        isurl = re.match(r'http|https', value.group(1))
        isbase64 = re.match(r'data:image/(.*);base64,', value.group(1))
        if (isbase64):
            imgbaseurl = re.sub(r'data:image/(.*);base64,', '', value.group(1))
            extension = re.match(r'data:image/(.*);base64,', value.group(1)).group(1)
            # date = str(int(time.time()))
            date = str(uuid.uuid4()).replace('-', '') + str(int(time.time()))
            img_name = date + '.' + extension
            # img_path = MEDIA_ROOT + self.article_path.format(datetime.datetime.now())
            img_path = MEDIA_ROOT + self.article_path
            if os.path.isfile(img_path + img_name):
                self.count += 1
                img_name = str(int(time.time())) + str(self.count) + '.' + extension
            img = base64.b64decode(imgbaseurl)
            fh = open(img_path + img_name, "wb")
            fh.write(img)
            fh.close()
            return "background-image: url('{}')".format('/media'+self.article_path + img_name)
        elif (isurl):
            data = requests.get(value.group(1)).content
            import imghdr
            extension = '.' + imghdr.what(None, data)
            print(extension)
            if extension not in ['.jpg', '.png', '.jpeg', '.svg', '.webp', '.gif']:
                return "background-image: url('{}')".format('')
            img_path = MEDIA_ROOT + self.article_path
            # extension = re.search(r'(\.jpeg|\.png|\.jpg|\.svg|\.webp|\.gif)', value.group(1)).group(1)
            # date = str(int(time.time()))
            date = str(uuid.uuid4()).replace('-', '') + str(int(time.time()))
            img_name = date + extension
            if os.path.isfile(img_path+img_name):
                self.count += 1
                img_name = str(int(time.time()))+str(self.count) + extension
            f = open(img_path + img_name, 'wb')
            f.write(data)
            f.close()
            return "background-image: url('{}')".format('/media'+self.article_path + img_name)

    def delImgFile(self, value):
        imgPath = BASE_DIR + value.group()[:-1]
        if os.path.isfile(imgPath):
            os.remove(imgPath)

    def startReptiles(self):
        # print('sdad')
        imgList = re.sub(r'<img(.*)src=\"(.*?)\"(.*?)>', self.changeImgUrl, self.html)
        imgBG = re.sub(r'background-image: url\(\'(.*?)\'\)', self.changeBgUrl, imgList)
        if self.type == 'put':
            self.delImg()
        return imgBG

    def delImg(self):
        # print(self.oldHTml)
        re.sub('\/media\/media\/uploads\/article\/(.*?)(\"|\')', self.delImgFile, self.oldHTml)
    # def updateReptiles(self):
    #     if(HOST_NAME in value.group(2)):
    #         regStr=value.group(2).index(HOST_NAME)+len(HOST_NAME)
    #         sqlUrl=value.group(2)[regStr:]
    #         return '<img{}src="{}"{}/>'.format(value.group(1), sqlUrl, value.group(3))
    #     if (HOST_NAME in value.group(1)):
    #         regStr = value.group(1).index(HOST_NAME) + len(HOST_NAME)
    #         sqlUrl = value.group(1)[regStr:]
    #         return "background-image: url('{}')".format(sqlUrl)
    #     return self.html


# BaseToImg(html='').startReptiles();

