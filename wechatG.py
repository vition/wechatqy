#!/usr/bin/env python
#-*-coding:utf-8-*-
import json
import urllib2
#全局常用的函数集合类
class WechatG(object):
	#这是类属性，存放微信token，共用
	access_token=""
	#post发送数据
	def post(self,url,data):
		postData=json.dumps(data,ensure_ascii=False)
		req=urllib2.urlopen(url,postData)
		return req.read()
	#get获取数据
	def get(self,url):
		getData=urllib2.urlopen(url)
		return getData.read()
