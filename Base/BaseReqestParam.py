from Base.BaseYaml import getYam
import os
from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def requestHead(path):
    '''
    请求头
    :return: 
    '''
    return getYam(path)


def paramsFilter(params):
    '''
    请求参数处理
    :param params:
    :return:
    '''

    result = {}
    for wap_key in params:
        for son_key in params[wap_key]:
            if params[wap_key]["error"] == "0" or params[wap_key]["error"] == "1" or params[wap_key]["error"] == "2": # 过滤和处理相关请求参数
                result[wap_key] = changeFormat(params[wap_key]["type"], params[wap_key]["input"])
            break
    return result


def changeFormat(key, param):
    '''
    请求参数类型处理
    :param key: 
    :param param: 
    :return: 
    '''
    param_type = {
        "str": lambda: str(param),
        "int": lambda: int(param),
        "float": lambda: float(param),
        "bool": lambda: bool(param)
    }
    return param_type[key]()

def readReq(param):
    '''
    读取请求的url
    :param param: 
    :return: 
    '''
    return param.split("|") # 1 用例id,2 用例介绍,3 url

def readParam(param):
    '''
    读取准备的pict参数
    param1:...
    param2:..
    :return: list
    '''
    result = []
    _param2 = ""
    for item in param:
        for key in item:
            tempParam = item[key].split("&")
            _param = ""
            for tItem in tempParam:
                tiParam = tItem.split("|")
                if len(tiParam) == 5:
                    _param = _param + "," + key + ":error:" + tiParam[0] + ":input:" + tiParam[1] + ":type:" + tiParam[
                        2] + ":" + tiParam[3] + ":" + tiParam[4]
                else:
                    _param = _param + "," + key + ":error:" + tiParam[0] + ":" + tiParam[1] + ":" + tiParam[2]
            _param2 = _param2 + "," + _param
            result.append(key + ":"+_param[1:])
            break
    return result


def readPictParam(paramRequestPath):
    '''
    读取本地e生成好了的接口请求参数
    :param paramRequestPath:  已经处理好的pict参数路径
    :return: list
    '''
    result = read(paramRequestPath)
    l_result = []
    if result:
        for info in range(len(result)):
            for item in range(len(result[info])):
                t_result = result[info][item].split(",")
                d_t = {}
                for i in t_result:
                    temp = i.split(":")
                    t = {}
                    t[temp[1]] = temp[2]
                    if len(temp) > 5: #如果大于5，说明全部参数为8：如 ：' {'rep': 'dict', 'type': 'str', 'input': '""', 'error': '2'}
                        t[temp[3]] = temp[4]
                        t[temp[5]] = temp[6]
                        t[temp[7]] = temp[8]
                    else:
                        t[temp[3]] = temp[4] # 参数至少
                    d_t[temp[0]] = t
                l_result.append(d_t)
    return l_result


def pairPatchParam(**kwargs):
    '''
       pict生成请求参数
       :param kwargs:
       params: 请求的参数列表，类型为list
       paramPath: 用例目录
       paramRequestPath： 已生成用例目录
       :return:
       '''

    for item in kwargs["params"]:
        write(kwargs["paramPath"], item)
    os.popen("pict " + kwargs["paramPath"] + ">" + kwargs["paramRequestPath"])
    time.sleep(1)

if __name__ == "__main__":
    # requestHead()
    loginY = getYam(PATH("../yaml/login.yaml"))

    result = readParam(loginY["param"])

    pairPatchParam(params=result, paramPath=PATH("../Log/param.log"), paramRequestPath=PATH("../Log/paramRequest.log"))
    # time.sleep(1)
    getParam = readPictParam(paramRequestPath=PATH("../Log/paramRequest.log"))

    # t = [{'ip': {'error': '3', 'rep': 'dict'}, 'format2': {'error': '3', 'rep': 'dict'}}, {'ip': {'input': '18.4.255.255', 'type': 'str', 'error': '0', 'rep': 'dict'}, 'format2': {'error': '1', 'rep': 'dict'}}, {'ip': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}, 'format2': {'error': '3', 'rep': 'dict'}}, {'ip': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}, 'format2': {'error': '1', 'rep': 'dict'}}, {'ip': {'error': '4', 'rep': 'dict'}, 'format2': {'error': '1', 'rep': 'dict'}}, {'ip': {'input': '18.4.255.255', 'type': 'str', 'error': '0', 'rep': 'dict'}, 'format2': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}}, {'ip': {'error': '1', 'rep': 'dict'}, 'format2': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}}, {'ip': {'error': '3', 'rep': 'dict'}, 'format2': {'error': '1', 'rep': 'dict'}}, {'ip': {'error': '1', 'rep': 'dict'}, 'format2': {'error': '3', 'rep': 'dict'}}, {'ip': {'error': '4', 'rep': 'dict'}, 'format2': {'error': '3', 'rep': 'dict'}}, {'ip': {'error': '3', 'rep': 'dict'}, 'format2': {'input': '1111', 'type': 'str', 'error': '0', 'rep': 'dict'}}, {'ip': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}, 'format2': {'input': '1111', 'type': 'str', 'error': '0', 'rep': 'dict'}}, {'ip': {'error': '4', 'rep': 'dict'}, 'format2': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}}, {'ip': {'error': '1', 'rep': 'dict'}, 'format2': {'input': '1111', 'type': 'str', 'error': '0', 'rep': 'dict'}}, {'ip': {'input': '18.4.255.255', 'type': 'str', 'error': '0', 'rep': 'dict'}, 'format2': {'error': '3', 'rep': 'dict'}}, {'ip': {'error': '4', 'rep': 'dict'}, 'format2': {'input': '1111', 'type': 'str', 'error': '0', 'rep': 'dict'}}, {'ip': {'error': '1', 'rep': 'dict'}, 'format2': {'error': '1', 'rep': 'dict'}}, {'ip': {'error': '3', 'rep': 'dict'}, 'format2': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}}, {'ip': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}, 'format2': {'input': '""', 'type': 'str', 'error': '2', 'rep': 'dict'}}, {'ip': {'input': '18.4.255.255', 'type': 'str', 'error': '0', 'rep': 'dict'}, 'format2': {'input': '1111', 'type': 'str', 'error': '0', 'rep': 'dict'}}]
    for item in getParam:
        print("----------")
        print(paramsFilter(item))