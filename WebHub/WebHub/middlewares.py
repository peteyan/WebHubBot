# encoding=utf-8
import json
import random

from user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """
    cookie = {
        'platform': 'pc',
        'ss': '367701188698225489',
        'bs': '%s',
        'RNLBSERVERID': 'ded6699',
        'FastPopSessionRequestNumber': '1',
        'FPSRN': '1',
        'performance_timing': 'home',
        'RNKEY': '40859743*68067497:1190152786:3363277230:1'
    }

    def process_request(self, request, spider):
        bs = ''
        for i in range(32):
            bs += chr(random.randint(97, 122))
        _cookie = json.dumps(self.cookie) % bs
        request.cookies = json.loads(_cookie)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://127.0.0.1:1081"  # http代理
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "http://127.0.0.1:1081"  # https代理
