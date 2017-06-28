import unittest
from datetime import datetime
from Base.BaseInit import *
from Base.BaseRunner import ParametrizedTestCase
# from Base.BaseStatistics import readInfo
from test.TestLogin import LoginTest
from test.TestSubmitApply import SubmitApplyTest

def runnerCase():
    starttime = datetime.now()
    init()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(SubmitApplyTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    print(u"花费："+str((endtime - starttime).seconds) + "秒")

    # readInfo(PATH("../Log/info.pickle"))
    destroy()

if __name__ == '__main__':
    runnerCase()
    # t = [{'wiseoper': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'fnNoaWt1bjE5ODk'}, 'name': {'rep': 'dict', 'error': '3'}}, {'wiseoper': {'rep': 'dict', 'error': '3'}, 'name': {'rep': 'dict', 'error': '3'}}, {'wiseoper': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'fnNoaWt1bjE5ODk'}, 'name': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'swx458348'}}, {'wiseoper': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'fnNoaWt1bjE5ODk1'}, 'name': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'swx458348'}}, {'wiseoper': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'fnNoaWt1bjE5ODk'}, 'name': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'swx4583481'}}, {'wiseoper': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'fnNoaWt1bjE5ODk1'}, 'name': {'rep': 'dict', 'error': '3'}}, {'wiseoper': {'rep': 'dict', 'error': '3'}, 'name': {'type': 'str', 'rep': 'dict', 'error': '0', 'input': 'swx458348'}}, {'wiseoper': {'rep': 'dict', 'error': '3'}, 'name': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'swx4583481'}}, {'wiseoper': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'fnNoaWt1bjE5ODk1'}, 'name': {'type': 'str', 'rep': 'dic', 'error': '1', 'input': 'swx4583481'}}]
    # for item in range(len(t)):
    #     print(t[item])
