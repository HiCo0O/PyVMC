#Accept: application/vnd.vmware.vmw.rest-v1+json
#Accept-Encoding#: gzip, deflate, br
#Accept-Language: zh-CN,zh;q=0.9
#Authorization: Basic ZmFuZzpGc2gxMjU0Li4=
#Connection: keep-alive
#Host: 127.0.0.1:8697
#Referer: http://127.0.0.1:8697/
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36

import base64
import urllib.request

class core:

    def __init__(self, username, password, host, path):
        self.username = username
        self.password = password
        self.host = host
        self.path = path
        self.header = {}
        self.authencode()
        self.header["Host"] = host
        self.header["Accept"] = "application/vnd.vmware.vmw.rest-v1+json"
        self.header["User-Agent"] = "VMWareWorkdStationContorl beta"
        self.header["Accept-Encoding"] = "Accept-Encoding:"
        self.header["Accept-Language"] = "zh-CN,zh;q=0.9"
        self.header["Connection"] = "keep-alive"
        self.header["Referer"]= "http://" + self.host + "/"

    def authencode(self):
        # 生成header中Authorization部分的内容，用于服务器认证，base64
        temp = (self.username + ":" + self.password).encode('utf8')
        temp = base64.b64encode(temp).decode()
        self.header["Authorization"] = "Basic " + temp

    def initRequest(self, path):
        temp = urllib.request.Request(self.header["Referer"]+'api/'+ path)
        for k,v in self.header.items():
            temp.add_header(k,v)
        self.Request = temp
        return temp

    def get(path, arg):
        pass

    def put(path, arg):
        pass

    def pst(path, arg):
        pass

    def delete(path, arg):
        pass
