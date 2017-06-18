import os

from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def init():

    mkFile(PATH("../Log/param.log"))
    mkFile(PATH("../Log/paramRequest.log"))

def destroy():
    removeFile(PATH("../Log/param.log"))
    removeFile(PATH("../Log/paramRequest.log"))