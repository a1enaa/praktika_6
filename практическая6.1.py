  #вариант:1 номер_1
a=[1,2,3,-1,-2,-3]
b=list(reversed(a))
print(max(a))
print(b)
  #номер_2
print('номер_2')
x=[1,2,5,0,7,0,6]
y=sum(x)/len(x)
for i in range(len(x)):
    if x[i]==0:
        x[i]=y
print(y)  #среднее значение
print(x)  #массив с замененнам нулевым элементом


