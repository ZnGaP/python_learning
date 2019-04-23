from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

date = []
weather = []
topTem = []
lowTem = []

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parserdata = ''
        self.__istem = 'no'

    def handle_starttag(self, tag, attrs):
        if ('class', ''):
            self.__parserdata = 'date'
        if ('class', 'wea') in attrs:
            self.__parserdata = 'weather'
        if ('class', 'tem') in attrs:
            self.__istem = 'yes'
        if tag == 'span' and self.__istem == 'yes':
            self.__parserdata = 'toptem'
        if tag == 'i' and self.__istem == 'yes':
            self.__parserdata = 'lowtem'
            self.__istem = 'no'

    def handle_endtag(self, tag):
        self.__parserdata = ''

    def handle_data(self, data):
        if self.__parserdata == 'date':
            if re.match(r'^\d\d[\u4e00-\u9fa5]（[\u4e00-\u9fa5]{2}）',data):
                date.append(data)
                print('日期：%s' % data)
        if self.__parserdata == 'weather':
            weather.append(data)
            print('天气：%s' % data)
        if self.__parserdata == 'toptem' and re.match(r'^\d\d℃?',data):
            topTem.append(data)
            print('最高温：%s℃' % data)
        if self.__parserdata == 'lowtem':
            lowTem.append(data)
            print('最低温：%s' % data)
            print('------------------------------------')

parser = MyHTMLParser()
URL = 'http://www.weather.com.cn/weather/101280101.shtml'
with request.urlopen(URL) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))

message = ''

for i in range(0, 6):
    message += date[i] + '  ' + weather[i] + '  最高温：' + topTem[i] + '  最低温：' + lowTem[i] + '\n'

if weather[0].find('雨') or weather[1].find('雨'):
    message += '雨天路滑，注意安全！出门记得带伞哦！'
print(message)     

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '871528607@qq.com'
password = 'fskqgtlrojtebede'
to_addr = 'lin_jx99@163.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText(message, 'plain', 'utf-8')
msg['From'] = _format_addr('欣欣 <%s>' % from_addr)
msg['To'] = _format_addr('渣男 <%s>' % to_addr)
msg['Subject'] = Header('来自欣欣的问候', 'utf-8').encode()
msg['Date'] = Header(time.strftime('%Y-%m-%d %X', time.localtime()), 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print('发送成功')
server.quit()