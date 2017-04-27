#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
sys.path.append("..")
from wechatG import WechatG
class Media (WechatG):
	"发送信息的类"
	def __init__(self):
		pass
	
	#text消息
	def upload(self,):
		pass
	

	#获取素材总数
	def get_count(self):
		url="https://qyapi.weixin.qq.com/cgi-bin/material/get_count?access_token="+WechatG.access_token
		print self.get(url)
	#获取素材列表
	def batchget(self,type):
		data={"type":type,"offset":0,"count":10}
		url="https://qyapi.weixin.qq.com/cgi-bin/material/batchget?access_token="+WechatG.access_token
		print self.post(url,data)
	
