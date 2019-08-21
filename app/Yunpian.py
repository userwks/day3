import requests
import random
import json
apikey = 'ed90007c967c1d817a1ee63c0405e1ad'
url = 'https://sms.yunpian.com/v2/sms/single_send.json'
class Yunpian():
    def __init__(self):
        self.apikey = apikey
        self.url = url

    def get_code(self):
        li = random.sample([i for i in range(10)],4)
        code = ''
        for i in li:
            code += str(i)
        return code
    def send_code(self,mobile,code):
        data = {
            'apikey':self.apikey,
            'mobile':mobile,
            'text':'您的验证码是%s'%code
        }
        re_data = requests.post(url=self.url,data=data)
        return json.loads(re_data.text)