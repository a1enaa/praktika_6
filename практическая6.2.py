    #вариант2 номер_1
a=[-1,4,-3,1,-2,3]
b=[]  #положительный список
c=[]  #отрицательный список
for i in range (len(a)):
    if a[i]>0:
        b.append(a[i])
    else:
        c.append(a[i])
print('b=',b)
print('c=',c)
     #номер_2
print('номер_2')
x=[1,-3,3,7,-5]
print('минимальный элемент:',min(x))
print('индекс минимального элемента:',x.index(min(x)))







