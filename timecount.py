# -*- coding: UTF-8 -*-
import time
def timecount(s):
    shijian=time.strptime(s,'%Y-%m-%d')
    days=shijian.tm_yday
    weeks=days/7
    if(days%7>0):
        weeks=weeks+1
    zhouji=shijian.tm_wday
    if(zhouji==6):
        weeks=weeks+1
    return shijian.tm_yday,weeks
    # return days,weeks,yutian
s='2017-1-8'
print timecount(s)
m='2016-1-8'
print timecount(m)