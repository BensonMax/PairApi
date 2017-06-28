import os
import unittest
from PageObject.PageSubmitApply import SubmitApply

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SubmitApplyTest(unittest.TestCase):

    def testsubmitApply(self):
        submitApply = SubmitApply(path=PATH("../yaml/submitApply.yaml"), initPath=PATH("../yaml/submitApp.yaml"))
        submitApply.operate(PATH("../Log/info.log"))
