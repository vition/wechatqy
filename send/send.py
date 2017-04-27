#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
sys.path.append("..")
from wechatG import WechatG
class Send (WechatG):
	"发送信息的类"
	def __init__(self):
		pass
	
	#text消息
	def text(self,agentid,touser,content,toparty="",totag=""):
		data={"touser":touser,"agentid":agentid,"msgtype":"text","text":{"content":content}}
		if toparty!="":	data["toparty"]=toparty
		if totag!="": data["totag"]=totag

		url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+WechatG.access_token	
		self.post(url,data)
