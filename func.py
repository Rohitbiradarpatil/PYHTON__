
"""***************
 *  PRIME NUMBER  *
 ****************
"""
"""
def prime(a):
    if a<2:
        return False
    for i in range(2,a-1):
        if((a%i)==0):
            return False
        else:
            return True           
       
x=prime(6)
if(x==True):
    print("PRIME")
else:
    print("NOT PRIME")
    """
"""***************
 *  FACTORIAL  *
 ****************
"""
""""
def fact(a):
    m=1
    for i in range(1,a+1):
        m*=i
    return m

print(fact(5))
"""
"""***************
 *  RUNNING SUM *
 ****************
"""

def runningsum(arr,size):
    m=1
    for i in range(1,size):
        arr[i]+=arr[i-1]
        
    return arr

arr = [1,2,3,4,5]   
x=runningsum(arr,5)
print(x)

