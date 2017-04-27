![mahua](https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=756974886,961366564&fm=58)
##wechatqy是什么?
一个用python写的微信企业号支持库



##wechatqy目前有哪些功能？

* 转动连接weixin
    * 通过设置corpid和 corpsecret获取access_token
    * 也可以直接设置access_token
* 通过send.text可以推送文本到指定的用户
* 通过media.get_count可以获取到素材数量
* 通过media.batchget获取到指定素材列表


##使用实例

```python
    wechat=Wechatqy()
    wechat.conf("corpid","corpsecret")
    print wechat.send.text(0,"用户id","这是一条测试的消息，收到请忽视")
```

