# -*- coding: UTF-8 -*-

def pxpd(s):
    i=0
    shengxu=1
    jiangxu=1
    while(i<s.__len__()-1):
        i=i+1
        if(s[i]>s[i-1]):
            jiangxu=0
        elif(s[i]<s[i-1]):
            shengxu=0
    if(shengxu):
        print 'UP'
    if(jiangxu):
        print 'DOWN'
    if(shengxu==jiangxu):
        print 'WRONG'



L=[12,3,13,1]
pxpd(L)