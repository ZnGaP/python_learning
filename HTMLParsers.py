from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parserdata = ''

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parserdata = 'name'
        if tag == 'time':
            self.__parserdata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parserdata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parserdata = 'location'
    
    def handle_endtag(self, tag):
        self.__parserdata = ''
    
    def handle_data(self, data):
        if self.__parserdata == 'name':
            print('会议名称：%s' % data)
        
        if self.__parserdata == 'time':
            print('会议时间：%s' % data)

        if self.__parserdata == 'year':
            print('会议年份：%s' % data)

        if self.__parserdata == 'location':
            print('会议地点：%s' % data)
            print('-------------------------------------------')

parser = MyHTMLParser()

URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))