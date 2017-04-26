#encoding:utf-8

class wechatqy(object):
	"微信企业号的类"
	def __init__(self):
		pass
	#config
	def conf(self,corpid,corpsecret):
		self.corpid=corpsecret
		self.corpsecret=corpsecret
	#access_token
	def access_token(self,token=""):
		"token为空，取token，否则设置token"
		if hasattr(self,token):
			if token!="":
				self.token=token
			else:
				return self.token
		else:
			print "请先配置corpid和corpsecret"

if __name__=='__main__':
	print "调用自己"
	wechat=wechatqy()
	print wechat.access_token()



