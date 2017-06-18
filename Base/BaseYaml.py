__author__ = 'shikun'
import yaml
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# -*- coding:utf-8 -*-
def getYam(path):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f)
            # print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")


if __name__ == "__main__":
    getYam(PATH("../yaml/login.yaml"))