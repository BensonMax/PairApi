import os
import unittest
from PageObject.PageSendEmail import SendEmail

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SendEmailTest(unittest.TestCase):

    def testSendEmail(self):
        sendEmail = SendEmail(path=PATH("../yaml/sendEmail.yaml"), initPath=PATH("../yaml/common.yaml"))
        sendEmail.operate(PATH("../Log/info.log"))
