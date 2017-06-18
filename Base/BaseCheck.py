def compare(exJson,factJson):
    '''
     {appStatus:0, content:[{}.{}]} 检查点
    :param exJson: 
    :param factJson: 
    :return: 
    '''
    isFlag = True
    if exJson.get("appStatus") == factJson.get("appStatus"):
        data2 = exJson.get("content")
        data3 = factJson.get("content")
        for item2 in data2:
            for item3 in data3:
                keys2 = item2.keys()
                keys3 = item3.keys()
                if keys2 == keys3: # 如果嵌套层的key完全相等
                     for key in keys2:
                        value2 = item2.get(key)
                        value3 = item3.get(key)
                        if type(value3)==type(value2):
                           pass
                        else:
                            isFlag = False
                            break
                else:
                    isFlag = False
                    break
    else:
        isFlag = False
    print(isFlag)
    return isFlag

def checkPointDict(exJson,factJson):
    '''
    {} 的检查点
    :param exJson: 
    :param factJson: 
    :return: 
    '''
    if exJson == factJson:
        return True
    return False
