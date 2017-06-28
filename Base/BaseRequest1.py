import asyncio
import aiohttp
import json
import requests
# -*- coding:utf-8 -*-
import time

from Base import BaseAsy


class request():
    def __init__(self, **kwargs):
        '''
        http请求的封装，传入dict
        :param req:
        '''
        self.req = kwargs
    def get(self, url, param):
        data = {}
        _url = self.req["protocol"] + self.req["host"] + ":" + str(self.req["port"]) + url
        print(_url +" get请求参数为:"+str(param))
        try:
            response = requests.get(url, params=param, headers=self.req["header"])
            response.encoding = 'UTF-8'
            if response.status_code == 200:
                data = json.loads(response.text)
            data["status_code"] = response.status_code
            print(data)
        except asyncio.TimeoutError:
            print("访问失败")
        return data
    def post(self,url, param):
        data = {}
        _url = self.req["protocol"] + self.req["host"] + ':' + str(self.req["port"]) + url
        print(_url + " post接口参数为:" + str(param))
        response = requests.post(_url,files=None, data=json.dumps(param),  headers=self.req["header"])
        response.encoding = 'UTF-8'
        if response.status_code == 200:
            data = json.loads(response.text)
        data["status_code"] = response.status_code
        print(data)

        return data
if __name__ == '__main__':
    pass
    # url = '/XXX/login'
    # # loop = asyncio.get_event_loop()
    # # tasks = []
    # protocol = "https://"
    # host = "host"
    # port= 8443
    # header = {}
    # f = request(header=header, host=host, protocol=protocol, port=port)
    # data = {'XXX': 'XXX', 'name': 'XXX'}
    # BaseAsy.asyn(f.post(url, param=data))
