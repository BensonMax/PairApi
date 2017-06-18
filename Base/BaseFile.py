__author__ = 'shikun'
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''
操作文件
'''


def checkFile(f_path):
    if not os.path.isfile(f_path):
        print('文件不存在' + f_path)
        # sys.exit()
        return False
    else:
        return True


def mkFile(f_path):
    with open(f_path, 'w', encoding="utf-8") as f:
        print("创建文件成功")
        pass


def write(f_path, line):
    if not checkFile(f_path):
        with open(f_path, "w", encoding="utf-8") as f:  # 如果文件不存在，则创建文件
            print("创建成功" + f_path)
    time.sleep(1)
    with open(f_path, 'a') as fileHandle:
        fileHandle.write(line + "\n")


def read(f_path):
    reslut = []
    print(f_path)
    with open(f_path, 'r', encoding="utf-8") as fileHandle:
        file_list = fileHandle.readlines()
        for i in file_list:
            temp = []
            temp.append(i.replace("\t", ",").strip("\n"))
            reslut.append(temp)
        reslut = reslut[1:]
    removeFile(PATH("../Log/param.log"))
    removeFile(PATH("../Log/paramRequest.log"))
    return reslut


def removeFile(f_path):
    if checkFile(f_path):
        os.remove(f_path)
        print("删除成功")
        # if __name__ == '__main__':
        #     bf = OperateFile("text.xml")
        #     if bf.check_file() == False:
        #         bf.mkdir_file()
        #     bf.write_txt("111")
