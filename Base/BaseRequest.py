import asyncio
import aiohttp
import json
# -*- coding:utf-8 -*-
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
            response = yield from aiohttp.request("GET", _url, headers=self.req["header"], params=param)
            string = (yield from response.read()).decode('utf-8')
            if response.status == 200:
                data = json.loads(string)
            else:
                print("data fetch failed for")
                print(response.content, response.status)
            data["status_code"] = response.status
            print(data)
        except asyncio.TimeoutError:
            print("访问失败")
        except UnicodeDecodeError:
            print("接口崩溃了")
        return data
    def post(self,url, param):
        data = {}
        _url = self.req["protocol"] + self.req["host"] + ':' + str(self.req["port"]) + url
        print(_url + " post接口参数为:" + str(param))
        try:
            response = yield from aiohttp.request('POST', _url, data=json.dumps(param), headers=self.req["header"])
            string = (yield from response.read()).decode('utf-8')
            if response.status == 200:
                data = json.loads(string)
            else:
                print("data fetch failed for")
                print(response.content, response.status)
            data["status_code"] = response.status
            print(data)
        except asyncio.TimeoutError:
            print("访问失败")
        return data
if __name__ == '__main__':
    url = '/wiseoper/login'
    # loop = asyncio.get_event_loop()
    # tasks = []
    protocol = "https://"
    host = "lfwiseopertest02.hwcloudtest.cn"
    port= 8443
    header = {"account": "sWX458348", "Content-Type": "application/json; charset=UTF-8","secrectKey": "Yzg0MTkyOTBjM2M1NDMyNmFkYjc2MzdlNGRhYjRiOTk=","appID": "app_2017030812000000011"}
    f = request(header=header, host=host, protocol=protocol, port=port)
    data = {'wiseoper': 'fnNoaWt1bjE5ODk', 'name': 'swx458348'}
    BaseAsy.asyn(f.post(url, param=data))
