#!/usr/bin/env python
#-*-coding:utf-8-*-

#全局常用的函数集合类
class WechatG(object):
	#post发送数据
	def post(self,url,data):
		postData=json.dumps(data,ensure_ascii=False)
		req=urllib2.urlopen(url,postData)
		return req.read()
	def test(self):
		print "测试·"
