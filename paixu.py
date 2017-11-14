# -*- coding: UTF-8 -*-
# 快速排序
# 从数列中取出一个数作为基准数->分区过程，最终结果小的数 基准数 大的数->再对左右区间重复分区过程，知道区间只有一个数
# s list l左标志位 r右标志位 paixu 0为升序 1为降序
def quick_sort(s,l,r,paixu=0):
    if(l>=r):
        return 'r必须大于l'
    if(not isinstance(s,list)):
        return '请传入list类型'
    if(l<r):
        i=l
        j=r
        x=s[l]
        # 一次分区过程
        while(i<j):
            # 先从右向左找
            # 降序排列
            if paixu:
                while (i < j and s[j] <= x):
                    j = j - 1
            else:
                while (i < j and s[j] >= x):
                    j = j - 1

            if(i<j):
                # 注意是把当前位置的数据赋值给基准数的位置
                s[i]=s[j]
                #i位置的数据确定了 则i坐标右移1个
                i=i+1
            # 从左向右找
            if paixu:
                while (i < j and s[i] >= x):
                    i = i + 1
            else:
                while (i < j and s[i] <= x):
                    i = i + 1

            if(i<j):
                s[j]=s[i]
                j=j-1
        # i=j时，找到了中间位置
        s[i]=x
        # 循环调用
        quick_sort(s,l,i-1,paixu)
        quick_sort(s,i+1,r,paixu)
    # 最后返回列表
    return s

# 进行测试
s=[33,43,22,66,2,54,7,39,55]
print s
print '升序排列'
print quick_sort(s,0,s.__len__()-1)
print '降序排列'
print quick_sort(s,0,s.__len__()-1,1)