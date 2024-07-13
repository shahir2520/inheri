import datetime
from functools import reduce
li = [3000,2000,50]
x =reduce(lambda x, y :  x+y, li)
print(x)

number1 =[1,2,3]
number2 =[4,5,6]
result = map(lambda x,y : x+y,number1,number2)
print(list(result))

import os

f = open('demo.txt','w')
f.write('file handling is very easy')
f = open('demo.txt','r')
print(f.readline())
f =open('demo.txt','r')
print(f.read())
f.close()
f =open('demo.txt','w')
f.write('hello shahir welcome to it company')
f = open('demo.txt','r')
print(f.read())
f.close()
f =open('demo.txt','w')
f.write('shahir is in it company with salary 90 thosand per month')
f = open('demo.txt','r')
print(f.readline())
f.close()

try:
    num1 = 10
    num2 = 2
    res = num1/num2
    print(res)
except:
    print('0 is not divisible by any number')
try:
    x = 7
    print(x)
except:
    print('something went wrong')
finally:
    print('this will always excuted')

from datetime import date
z = datetime.datetime(1947,1,22,23,24)
print(z.year)
print(z.month)
print(z.day)
print(z.strftime("%A"))

from datetime import datetime,timedelta
curr_date = datetime.now()
print(curr_date)
new_date = curr_date -timedelta(days=10)
print(new_date)

from datetime import date
curr_date = date.today()
print(curr_date)

import datetime
z = datetime.datetime.now()
print('the time is',z)


#JSOn java script object notation

import json
json_str = '{"name":"shahir","language":["English","Marathi"]}'
print(type(json_str))
lan_dic = json.loads(json_str)
print(type(lan_dic))
print(lan_dic)
print(lan_dic['language'][1])

import json
json_str = '{"name:"shahir","language":["python","java"]}'
print(type(json_str))
lang_dict = json.loads(json_str)
print(type(lang_dict))
print(lang_dict['language'][0])


#dump
import json
dic = {
    "name" :["json",'os','math'],
    "age": 21,
    "address": "mumbai"

}

json_date =json.dumps(dic)
print(json_date)
print(type(json_date))


