import unittest
from datetime import datetime

import xlsxwriter

from Base.BaseInit import *
from Base.BaseReport import OperateReport
from Base.BaseRunner import ParametrizedTestCase
# from Base.BaseStatistics import readInfo
from Base.BaseStatistics import readInfo
from test.TestLogin import LoginTest
from test.TestRevokeApply import RevokeApplyTest
from test.TestSubmitApply import SubmitApplyTest
from test.TestQueryOperLog import QueryOperLogTest
from test.TestQueryApply import QueryApplyTest
from test.TestApproveApply import ApproveApplyTest
from test.TestRejectApplyByState import RejectApplyByStateTest
from test.TestRejectApply import RejectApplyTest
from test.TestReqUploadFile import ReqUploadFileTest
from test.TestGetUserInfo4Service import GetUserInfo4ServiceTest
from test.TestGetApplyStepInfo import GetApplyStepInfoTest
from test.TestGetApplyListByAccount import GetApplyListByAccountTest
from test.TestApproveApplyByState import ApproveApplyByStateTest
from test.TestSubmitUploadResult import SubmitUploadResultTest
from test.TestGetBestIP import GetBestIPTest
from test.TestSendEmail import SendEmailTest
from test.TestChangeApprover4Service import  ChangeApprover4ServiceTest
from test.TestQueryGroupInfoAndUserInfo import QueryGroupInfoAndUserInfoTest
from test.TestSubmitExecResult import SubmitExecResultTest
# -*- coding:utf-8 -*-

def runnerCase():
    starttime = datetime.now()
    init()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    suite.addTest(ParametrizedTestCase.parametrize(SubmitExecResultTest))
    suite.addTest(ParametrizedTestCase.parametrize(SendEmailTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    print(u"花费："+str((endtime - starttime).seconds) + "秒")

    info = readInfo(PATH("../Log/info.log"))
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("接口测试")
    re = OperateReport(wd=workbook)
    re.report(worksheet, data=info)
    destroy()
def conselog():
    result = []
    t = [
    [
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001"
                },
                "appId": {
                    "rep": "dic",
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数不传"
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数不传"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dic",
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数不传"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数不传"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dic",
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011"
                },
                "appId": {
                    "rep": "dic",
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数不传"
                },
                "digest": {
                    "rep": "dic",
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数不传"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数不传"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数不传"
                },
                "digest": {
                    "rep": "dic",
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数不传"
                },
                "digest": {
                    "rep": "dic",
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dic",
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数不传"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数不传"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数不传"
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数不传"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dic",
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dict",
                    "info": "transactionID参数不传"
                },
                "appId": {
                    "rep": "dic",
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dic",
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011"
                },
                "appId": {
                    "rep": "dict",
                    "info": "appId参数不传"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409"
                }
            }
        },
        {
            "method": "POST",
            "result": {
                "data": {
                    "errorInfo": {
                        "errorInfoUrl": "",
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400,
                "info": "",
                "resultCode": "wiseoper.system.default.exception.10001"
            },
            "url": "/cloudmanager/api/IUniEA/submitExecResult",
            "param": {
                "transactionID": {
                    "rep": "dic",
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011"
                },
                "appId": {
                    "rep": "dic",
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004"
                },
                "resultItemList": {
                    "rep": "dict",
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\""
                },
                "digest": {
                    "rep": "dict",
                    "info": "digest参数不传"
                }
            }
        }
    ]
]
    for i in t[0]:
        ts = []
        for k in i["param"]:
            ts.append(i["param"][k]["info"])
            # print(i["param"][k]["info"])
        result.append(ts)
    t = 0
    for key in result:
        s = ""
        t = t + 1
        for tem in key:
            s = s + tem + ","
        # print(str(t) + "."+ s +"发送请求")
        # print(s +"发送请求:检查返回码和返回信息")
if __name__ == '__main__':
    runnerCase()
    # conselog()

