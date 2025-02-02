import math
x = [15.6,15.8,16.2,16.3,15.9,15.5,15.9,16.0,15.8]
res = 0
mean = 15.75
for i in x:
    res+= (i-mean)**2

res/=9
math.sqrt(res)
print(res)