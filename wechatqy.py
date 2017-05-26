#!/usr/bin/env python
#-*-coding:utf-8-*-
from wechatG import WechatG#引入全局类
from send.send import Send#引入发送信息的类
from media.media import Media#引入发送信息的类
import urllib2
import time
import json
import os
class Wechatqy(WechatG):
	"微信企业号的类"
	def __init__(self):
		self.send=Send()#用来发送消息的
		self.media=Media()#媒体操作类
	#config
	def conf(self,corpid,corpsecret):
		self.corpid=corpid
		self.corpsecret=corpsecret
		WechatG.access_token=self.read_token()
		
	#从服务器里获取access_token
	def get_token(self):
		#token=urllib2.urlopen("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+self.corpid+"&corpsecret="+self.corpsecret)
		tokenJson=self.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+self.corpid+"&corpsecret="+self.corpsecret)
		nowTime=int(time.time())
		#tokenJson=token.read()
		tokenDict=eval(tokenJson)
		tokenDict["expires_in"]=7200+nowTime
		tokenFile=open("access_token","w+")
		tokenFile.write(json.dumps(tokenDict))
		return tokenDict["access_token"]
	
	#读取 access_token，可能从本地取值
	def read_token(self):
		if os.path.exists("access_token"):
			tokenFile=open("access_token","a+")
                	tokenStr=tokenFile.read()
			tokenJson=eval(tokenStr)
			if tokenJson["expires_in"]>int(time.time()):
				return tokenJson["access_token"]
			else:
				return self.get_token()
		else:
			return self.get_token()
		
	#设置或者读取access_token
	def access_token(self,token=""):
		"token为空，取token，否则设置token"
		if token!="":
			WechatG.access_token=token
		else:
			if WechatG.access_token!="":
				return WechatG.access_token
			else:
				print "请先配置corpid和corpsecret"
if __name__=='__main__':
	wechat=Wechatqy()
	wechat.conf("","")
	#发送测试
	#print wechat.send.text(0,"1000000107","这是一条测试的消息，收到请忽视")
	#获取素材测试
	#wechat.media.get_count()
	wechat.media.batchget("image")
	wechat.media.batchget("mpnews")
	wechat.media.batchget("voice")
	wechat.media.batchget("video")
	wechat.media.batchget("file")



