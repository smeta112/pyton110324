
def pyram(rows):
    for i in range(rows,0,-1):
        for j in range(0,i):
            print("*", end='')
        if i>1: print("\n")

pyram(5)
#обратка







"""
def py(n):
    for i in range(n,0,-1):
        print("*"*i)

py(5)
"""

'''
def pyram(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*", end='')
        if(i+1)<rows: print("/n")

pyram(5)


*
**
***
****
*****
'''



