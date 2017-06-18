from Base import BaseAsy
from Base.BaseReqestParam import readParam, pairPatchParam, readPictParam, readReq, paramsFilter, requestHead
from Base.BaseYaml import getYam
from Base.BaseRequest import request
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Login:
    '''
    kwargs: 
    path: 用例文件目录
    initPath： 请求头部目录
    '''

    def __init__(self, **kwargs):
        self.path = kwargs["path"]  # 用例yaml目录
        self.param = getYam(self.path)["param"]  # 请求参数
        self.req = getYam(self.path)["req"]  # 请求url
        self.readParam = readParam(self.param)  # 读取并处理请求参数
        pairPatchParam(params=self.readParam, paramPath=PATH("../Log/param.log"),
                       paramRequestPath=PATH("../Log/paramRequest.log"))  # pict生成参数
        self.getParam = readPictParam(paramRequestPath=PATH("../Log/paramRequest.log"))  # 得到pict生成的参数
        self.readReq = readReq(self.req)  # 0 用例id,1 用例介绍,2 url,3 mehtod
        print(self.readReq)
        self.head = requestHead(kwargs["initPath"]) # initPath 请求头准备
        print(self.head)
        # self.head = requestHead(PATH("../yaml/init.yaml"))  # protocol ,header,port,host,title

    '''
    发请求
    '''

    def operate(self):
        for item in self.getParam:
            param = paramsFilter(item) # 过滤接口,如果有其他加密，可以自行扩展
            f = request(header=self.head["header"], host=self.head["host"], protocol=self.head["protocol"], port=self.head["port"])
            if self.readReq[3] == "POST":
                BaseAsy.asyn(f.post(self.readReq[2], param=param))
            else:
                BaseAsy.asyn(f.get(self.readReq[2], param=param))
