#!/usr/bin/env python
#-*-coding:utf-8-*-

class Send (object):
	"发送信息的类"
	def __init__(self,token):
		self.token=token
	

	#text消息
	def text(self,touser,toparty,totag,agentid,content):
		urllib2
