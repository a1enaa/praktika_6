  #вариант:8 номер_1
import math
a=[4,3,7]
b=math.prod(a)
print(sum(a))
print(b)
  #номер_2
print('номер_2')
x=[1,3,0,4]
y=sum(x)/len(x)
for i in range(len(x)):
    if x[i]==0:
        x[i]=y
print(y)  #среднее значение
print(x)  #замененный нулевой элемент

