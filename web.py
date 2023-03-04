import requests
import re

urls = input('请输入web网址：')
url = f"{urls}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
resp = requests.get(url, headers=header)
# print(resp.text)
obj = re.compile(f'href="//(?P<web>.*?)"', re.S)
web_1 = obj.finditer(resp.text)
for i in web_1:
    print(i.group('web'))
    with open('C:\\Users\lenovo\Desktop\\url.txt', 'a') as file:
        # with open('/root/桌面/url.txt', 'a') as file:
        print(i.group('web'), file=file)
