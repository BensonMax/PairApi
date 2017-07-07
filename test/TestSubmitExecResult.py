import os
import unittest
from PageObject.PageSubmitExecResult import SubmitExecResult

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SubmitExecResultTest(unittest.TestCase):

    def testSubmitExecResult(self):
        submitUploadResult = SubmitExecResult(path=PATH("../yaml/submitExecResult.yaml"), initPath=PATH("../yaml/submitApp.yaml"))
        submitUploadResult.operate(PATH("../Log/info.log"))
