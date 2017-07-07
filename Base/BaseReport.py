import xlsxwriter
class OperateReport:
    def __init__(self, wd):
        self.wd = wd
    def report(self, worksheet, data):
        self.init(worksheet)
        self.detail(worksheet, data)
        self.close()
        # self.pie(self.wd, worksheet)
    def init(self, worksheet):
        # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:E1', '接口测试报告', define_format_H1)
        # worksheet.merge_range('A2:D2', '测试概括', define_format_H2)
        _write_center(worksheet, "A2", '接口名', self.wd)
        _write_center(worksheet, "B2", '接口URL', self.wd)
        _write_center(worksheet, "C2", '接口方法', self.wd)
        _write_center(worksheet, "D2", '接口参数', self.wd)
        _write_center(worksheet, "E2", '接口结果', self.wd)
    def pie(self, workbook, worksheet):
     chart1 = workbook.add_chart({'type': 'pie'})
     chart1.add_series({
         'name': '自动化测试统计',
         'categories': '=测试总况!$C$3:$C$4',
         'values': '=测试总况!$D$3:$D$4',
     })
     chart1.set_title({'name': '自动化测试统计'})
     chart1.set_style(10)
     worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
        # pie(self.wd, worksheet)
    def detail(self, worksheet, data):
        temp = 3
        for item in data:
            for k in item:
                _write_center(worksheet, "A" + str(temp), k["title"], self.wd)
                _write_center(worksheet, "B" + str(temp), k["url"], self.wd)
                _write_center(worksheet, "C" + str(temp), k["method"], self.wd)
                _write_center(worksheet, "D" + str(temp), "请求参数:"+ str(k["param"]), self.wd)
                if k["result"].get("data", "#") != "#":
                    _write_center(worksheet, "E" + str(temp), "响应码:" + str(k["result"]["status_code"]) + "\n响应结果:" +str(k["result"]["data"]), self.wd)
                else:
                    _write_center(worksheet, "E" + str(temp), "响应码:" + str(k["result"]["status_code"]) + "\n响应结果为空", self.wd)
                temp = temp + 1

    def close(self):
        self.wd.close()
def get_format(wd, option={}):
    return wd.add_format(option)

def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))
def set_row(worksheet, num, height):
    worksheet.set_row(num, height)


if __name__ == '__main__':
    info = [
    [
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.login.error.1005",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 409
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数正确",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 400
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数不传",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "resultList": {
                        "result": "success",
                        "token": "F766C6B3FD25BC20C7DE94D0F4EB97D7:4D678D5A792E13864C9D324D1C84BB1299D91D50F7F131C3825D3ED0D8FC5AFFE9FEC3E076468498967B04E1026D049D"
                    }
                },
                "status_code": 200
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数正确",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数正确",
                    "type": "str",
                    "input": "swx458348",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.login.error.1011",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 409
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数错误",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk1",
                    "rep": "dic"
                },
                "name": {
                    "info": "name参数正确",
                    "type": "str",
                    "input": "swx458348",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.login.error.1005",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 409
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数正确",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数错误",
                    "type": "str",
                    "input": "swx4583481",
                    "rep": "dic"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.login.error.1005",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 409
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数错误",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk1",
                    "rep": "dic"
                },
                "name": {
                    "info": "name参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 400
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数不传",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数正确",
                    "type": "str",
                    "input": "swx458348",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.system.default.exception.10001",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 400
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数不传",
                    "rep": "dict"
                },
                "name": {
                    "info": "name参数错误",
                    "type": "str",
                    "input": "swx4583481",
                    "rep": "dic"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorCode": "wiseoper.login.error.1005",
                        "errorInfoUrl": ""
                    }
                },
                "status_code": 409
            },
            "title": "登录",
            "url": "http://10.22.0.35:5555/login",
            "method": "POST",
            "param": {
                "wiseoper": {
                    "info": "wiseoper参数错误",
                    "type": "str",
                    "input": "fnNoaWt1bjE5ODk1",
                    "rep": "dic"
                },
                "name": {
                    "info": "name参数错误",
                    "type": "str",
                    "input": "swx4583481",
                    "rep": "dic"
                }
            }
        }
    ],
    [
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004",
                    "rep": "dic"
                },
                "transactionID": {
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9",
                    "rep": "dic"
                },
                "appId": {
                    "info": "appId参数不传",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数不传",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数不传",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9",
                    "rep": "dic"
                },
                "appId": {
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004",
                    "rep": "dic"
                },
                "transactionID": {
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011",
                    "rep": "dic"
                },
                "resultItemList": {
                    "info": "resultItemList参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数不传",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9",
                    "rep": "dic"
                },
                "appId": {
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数不传",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数错误",
                    "type": "str",
                    "input": "2491295e0f01ac63403b55b5a059548c9421b5466c71024155b1ff833341ba9",
                    "rep": "dic"
                },
                "appId": {
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数正确",
                    "type": "str",
                    "input": "000300000020170629200214000001",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数正确",
                    "type": "str",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011",
                    "rep": "dic"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数不传",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数不传",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数不传",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数不传",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数值类型错误",
                    "type": "int",
                    "input": "0003",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011",
                    "rep": "dic"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004",
                    "rep": "dic"
                },
                "transactionID": {
                    "info": "transactionID参数不传",
                    "rep": "dict"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数正确",
                    "type": "str",
                    "input": "04c5235c635d6911ba29314712137ae3e717525096cda426e48656c336667409",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数不传",
                    "rep": "dict"
                },
                "transactionID": {
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011",
                    "rep": "dic"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        },
        {
            "result": {
                "data": {
                    "errorInfo": {
                        "errorDesc": "",
                        "errorInfoUrl": "",
                        "errorCode": "wiseoper.system.default.exception.10001"
                    }
                },
                "status_code": 400
            },
            "title": "提交执行结果",
            "url": "http://10.22.0.32:9030/cloudmanager/api/IUniEA/submitExecResult",
            "method": "POST",
            "param": {
                "digest": {
                    "info": "digest参数不传",
                    "rep": "dict"
                },
                "appId": {
                    "info": "appId参数错误",
                    "type": "str",
                    "input": "0004",
                    "rep": "dic"
                },
                "transactionID": {
                    "info": "transactionID参数错误",
                    "type": "str",
                    "input": "0003000000201706281437530000011",
                    "rep": "dic"
                },
                "resultItemList": {
                    "info": "resultItemList参数错误",
                    "type": "str",
                    "input": "\"111\"",
                    "rep": "dict"
                }
            }
        }
    ]
]
    # for item in info:
    #     # print(item)
    #     for item1 in item:
    #         print(item1)
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    re = OperateReport(wd=workbook)
    re.report(worksheet, data=info)
    re.close()




