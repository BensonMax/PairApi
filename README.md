# ˵��
ȫ��ż�ӿ����ɲ���

# ���� 
* python3.4  asyncio aiohttp 
* unittest������
* objectpage
* ����ά���õ�YMAL
* ����PICTȫ��ż���ɽӿڲ�


# ����



**����init.yaml**

```
title: XXXX�ӿڲ���
host: lfwiseopertest02.hwcloudtest.cn
port: 8443
protocol: https://
header: {account": "XX", "Content-Type": "application/json; charset=UTF-8","secrectKey": "XXX=","appID": "XX"}
```


# ʵ��-��¼


**��������yaml**

```
req: 1001|��¼|/wiseoper/login|POST
param:
  - name: 0|swx458348|str|rep|dict&1|swx4583481|str|rep|dic&3|rep|dict
  - wiseoper: 0|fnNoaWt1bjE5ODk|str|rep|dict&1|fnNoaWt1bjE5ODk1|str|rep|dic&3|rep|dict
  
#error: 0������1�����ֵ��2���ʹ���,3�����ֶΣ�4��������չ�������С
#rep�������Ǽ��㣬֧��
#{} ,��ӦkeyΪDict
#{[]},��ӦkeyΪDictList
#{[{},{}]} ��ӦkeyΪDictListDict

```



**PageObject**

```
class Login:
    '''
    kwargs: 
    path: �����ļ�Ŀ¼
    initPath�� ����ͷ��Ŀ¼
    '''

    def __init__(self, **kwargs):
        self.path = kwargs["path"]  # ����yamlĿ¼
        self.param = getYam(self.path)["param"]  # �������
        self.req = getYam(self.path)["req"]  # ����url
        self.readParam = readParam(self.param)  # ��ȡ�������������
        pairPatchParam(params=self.readParam, paramPath=PATH("../Log/param.log"),
                       paramRequestPath=PATH("../Log/paramRequest.log"))  # pict���ɲ���
        self.getParam = readPictParam(paramRequestPath=PATH("../Log/paramRequest.log"))  # �õ�pict���ɵĲ���
        self.readReq = readReq(self.req)  # 0 ����id,1 ��������,2 url,3 mehtod
        print(self.readReq)
        self.head = requestHead(kwargs["initPath"]) # initPath ����ͷ׼��
        print(self.head)
        # self.head = requestHead(PATH("../yaml/init.yaml"))  # protocol ,header,port,host,title

    '''
    ������
    '''

    def operate(self):
        for item in self.getParam:
            param = paramsFilter(item) # ���˽ӿ�,������������ܣ�����������չ
            f = request(header=self.head["header"], host=self.head["host"], protocol=self.head["protocol"], port=self.head["port"])
            if self.readReq[3] == "POST":
                BaseAsy.asyn(f.post(self.readReq[2], param=param))
            else:
                BaseAsy.asyn(f.get(self.readReq[2], param=param))

```


**test**

```
from PageObject.PageLogin import Login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(unittest.TestCase):

    def testLogin(self):
        login = Login(path=PATH("../yaml/login.yaml"), initPath=PATH("../yaml/init.yaml"))
        login.operate()
)

```



# �������ʵ��

```
from Base.BaseRunner import ParametrizedTestCase
from test.TestLogin import LoginTest

def runnerCase():
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
if __name__ == '__main__':
    runnerCase()
```



# ���ִ�й���
```
https://XXX post�ӿڲ���Ϊ:...
Task ret: {'status_code': 409}
https://XXX post�ӿڲ���Ϊ:{}
{'status_code': 400}
Task ret: {'status_code': 400}
https://XXX/login post�ӿڲ���Ϊ:....
{'status_code': 200, 'resultCode': 0, 'info': 'Success', '...
https:/...r/login post�ӿڲ���Ϊ:{'name': 'XXX', 'pwd': 'XXX'}
{'status_code': 409}
......

```

# ����
* ���������ͳ�Ʊ���
* �������ϼ���ļ��








