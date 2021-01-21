import time
import unittest

from dingding_client.notice_client import NoticeClient


class SendMessageToDingDingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app_key = ""
        self.app_secret = ""
        self.api_url = ""

    def testSend(self):
        client = NoticeClient(app_key=self.app_key, app_secret=self.app_secret, api_url=self.api_url)
        try:
            # 第一个参数是一个列表，表示要发送给谁
            # 第二个参数也是一个列表， 表示mq消息队列
            client.send({"message": "测试数据"}, ["s4261"])
            client.send({"message": "测试数据"}, ["s4261"])
            print("测试")
        except Exception as e:
            print(e)

        while 1:
            time.sleep(10)