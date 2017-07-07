# ˵��
ȫ��ż�ӿ����ɲ���

# ���� 
* python3.4  ���߳�
* unittest������
* objectpage
* ����ά���õ�YMAL
* ����PICTȫ��ż���ɽӿڲ�


# ����



**����init.yaml**

```
title: XXXX�ӿڲ���
host: baidu.com
port: 8443
protocol: https://
header: {account": "XX", "Content-Type": "application/json; charset=UTF-8","secrectKey": "XXX=","appID": "XX"}
```


# ʵ��-��¼


**��������yaml**

```
req: 1001|��¼|/XX/login|POST
param:
  - name: 0|swx458348|str|rep|dict&1|swx4583481|str|rep|dic&3|rep|dict
  - XX: 0|fnNoaWt1bjE5ODk|str|rep|dict&1|fnNoaWt1bjE5ODk1|str|rep|dic&3|rep|dict
  
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

   # ��������
    def request(self, item):
        app = {}
        param = paramsFilter(item)  # ���˽ӿ�,������������ܣ�����������չ
        print(param)
        f = request(header=self.head["header"], host=self.head["host"], protocol=self.head["protocol"],
                    port=self.head["port"])
        app["url"] = self.readReq[2]
        app["param"] = writeResultParam(item)
        app["method"] = self.readReq[3]
        if self.readReq[3] == "POST":
            app["result"] = f.post(self.readReq[2], param=param)
        else:
            app["result"] = f.get(self.readReq[2], param=param)
        self.data.append(app)

    def operate(self, path):
        '''
        ������
        :param path: ͳ�Ƶ�path
        :return: 
        '''
        threads = []
        for item in range(len(self.getParam)):
            threads.append(BThread(self.request(self.getParam[item])))
        for j in range(len(self.getParam)):
            threads[j].start()
        for k in range(len(self.getParam)):
            threads[k].join())

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



# ���ִ�й���1 

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

![](Img/report.PNG)


# ����
* �������ϼ���ļ��








