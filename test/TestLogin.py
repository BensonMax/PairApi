import os
import unittest
from PageObject.PageLogin import Login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(unittest.TestCase):

    def testLogin(self):
        login = Login(path=PATH("../yaml/login.yaml"), initPath=PATH("../yaml/init.yaml"))
        login.operate(PATH("../Log/info.log"))
