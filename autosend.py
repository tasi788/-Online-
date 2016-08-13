#!/usr/bin/python
# coding: utf-8
from line import LineClient, LineGroup, LineContact
from time import strftime
import time
import datetime, uniout, random
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('apitoken.txt')
line_login = parser.get('apitoken', 'line_login')
line_passwd = parser.get('apitoken', 'line_passwd')
random_num = random.randint(0,4)
head = parser.get('word', str(random_num))

#line登入
try:
    client = LineClient(line_login, line_passwd)
    print 'Login success'
except:
    print 'Login failed'

n = 1
group = client.getGroupByName('聊天室')

while True:
    #時序調整
    if strftime("%H:%M:%S")=='00:00:00':
        group.sendMessage(str(head))
        random_num = random.randint(0,3)
        head = parser.get('word', str(random_num))
        time.sleep(1)
    #防呆 每小時load msg
    elif strftime("%M:%S")=='00:00':
        messages = group.getRecentMessages(count=10)
