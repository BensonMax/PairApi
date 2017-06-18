import unittest
from datetime import datetime
from Base.BaseInit import *
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseStatistics import readInfo
from test.TestLogin import LoginTest

def runnerCase():
    starttime = datetime.now()
    init()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    print(u"花费："+str((endtime - starttime).seconds) + "秒")

    # readInfo(PATH("../Log/info.pickle"))
    destroy()

if __name__ == '__main__':
    runnerCase()
