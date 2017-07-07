import os

from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def init():
    # destroy()
    mkFile(PATH("../Log/info.log"))
    time.sleep(1)


def destroy():
    removeFile(PATH("../Log/info.log"))
