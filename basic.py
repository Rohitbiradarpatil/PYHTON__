

# string concatination(imutable)
""""
var = "rohit"
var4 = ' '
var1 = "sharma"
var2 = var+var4+var1
print(var2)

# input
#var =int(input("whats your age"))
#print(var)
"""
#calculator
""""
data = input("ENTER OPERATION ").split()
print(int(data[0]),data[1],int(data[2]))
op =data[1]
x= int(data[0])
y =int(data[2])
if(op=='+'):
    print(y+x)
elif(op=='-'):
 print(x-y)
elif(op=='*'):
 print(x*y)
elif(op=='/'):
    print(x/y)
elif(op=='^'):
    print(x^y)
else:
    print("INVALID OPERATION")
"""
# list (are mutable)
""""
lis =["hello",'200',"bro","bye"]
print(lis)
lis.append("ohh")
print(lis)
input = input("ENTER THE ELEMENT TO ADDED")
lis.append(input)
lis"""

for i in range(0,13):
    i=i+1
print(i)
    