#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import json
import time
import os
class wechatqy(object):
	"微信企业号的类"
	def __init__(self):
		self.token=""
		pass
	#config
	def conf(self,corpid,corpsecret):
		self.corpid=corpid
		self.corpsecret=corpsecret
		self.token=self.read_token()
		
	#get access_token
	def get_token(self):
		token=urllib2.urlopen("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+self.corpid+"&corpsecret="+self.corpsecret)
		nowTime=int(time.time())
		tokenJson=token.read()
		tokenDict=eval(tokenJson)
		tokenDict["expires_in"]=7200+nowTime
		tokenFile=open("access_token","a+")
		tokenFile.write(json.dumps(tokenDict))
		return tokenDict["access_token"]
	
	#read access_token
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
		
	#access_token
	def access_token(self,token=""):
		"token为空，取token，否则设置token"
		if token!="":
			self.token=token
		else:
			if self.token!="":
				return self.token
			else:
				print "请先配置corpid和corpsecret"

if __name__=='__main__':
	#print "调用自己"
	wechat=wechatqy()
	wechat.conf("wx650b23fa694c8ff7","w_oV6aNTMaNUrOjwah0zupDxnWeYmtDR3QiUcD3Uqf584CpwYPB-U79QuhLLD_eJ")
	print wechat.access_token()





