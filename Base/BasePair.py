import os
from Base.BaseFile import *
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def pictParam(**kwargs):
    '''
    pict处理请求的参数
    :param kwargs:
    params: 请求的参数列表，类型为list
    paramPath: 用例目录
    paramRequestPath： 已生成用例目录
    :return:
    '''

    # path = PATH("../Log/param.log")
    for item in kwargs["params"]:
        write(kwargs["paramPath"], item)
    os.popen("pict " + kwargs["paramPath"] + ">"+kwargs["paramRequestPath"])


def readPictParam(pict_params):
    '''
    读取本地e生成好了的接口请求参数
    :param pict_params:  本地路径
    :return: list
    '''
    path = PATH("../Log/param.log")
    result = read(path)
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
                    if len(temp) >= 4:
                        t[temp[3]] = temp[4]
                        t[temp[5]] = temp[6]
                    d_t[temp[0]] = t
                l_result.append(d_t)
    return l_result
if __name__ == "__main__":
    t = readPictParam(Const.PICT_PARAMS_RESULT)
    print(t)