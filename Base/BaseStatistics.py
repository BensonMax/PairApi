import pickle


def readInfo(path):
    data = []
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
            print(data)
        except EOFError:
            data = []
            print("读取文件错误")
    print("------read-------")
    print(data)
    return data



def writeInfo(data="", path="data.pickle"):
    """

    :type data: list
    """
    # data = []
    # data.append([{"a":"b"}])
    # data.append([{"c":"d"}])

    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        print("------writeInfo-------")
        print(result)
        pickle.dump(result, f)