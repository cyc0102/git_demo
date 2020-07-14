import numpy as np
max_n=100
array=np.zeros([max_n])

def f(n):
    if (array[n]!=0):
        return array[n]
    if (n==1):
        answer=1
    else:
        answer=(n*f(n-1))
    array[n]=answer
    return answer
# print (f(5))
print (f(6))
print (array)
print (f(5))