# -*- coding: UTF-8 -*-
# if equal is up jiashe [5,5]wei shengxu
def pxpd(s):
    i=0
    shengxu=1
    jiangxu=1
    while(i<s.__len__()-1):
        i=i+1
        if(s[i]>=s[i-1]):
            jiangxu=0
        elif(s[i]<s[i-1]):
            shengxu=0
    if(shengxu):
        print 'UP'
    if(jiangxu):
        print 'DOWN'
    if(shengxu==jiangxu):
        print 'WRONG'



L=[3,5,5,6,7,9]
pxpd(L)
S=[16,8,5,3,1]
pxpd(S)
H=[3,4,5,12,6,6,3]
pxpd(H)