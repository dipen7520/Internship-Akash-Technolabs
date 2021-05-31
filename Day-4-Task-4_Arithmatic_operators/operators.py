print("------------------Operators--------------------")

x=10
y=6
z=20
lst = [10,20,30,40,50,60,'hello','Guys']
print("x:",x)
print("y:",y)
print('z:',z)
print("lst:",lst)
print("------------------------------------------------")

print("<-----Arithmetic operators----->")
print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y)
print("x//y=",x//y)
print("x%y=",x%y)

print("<-----Comparision Operators----->")
print(" x>y =",x>y)
print(" x<y =",x<y)
print(" x==y =",x==y)
print(" x>=y =",x>=y)
print(" x<=y =",x<=y)
print(" x!=y =",x!=y)

print("<----Logical Operators---->")
print("-----and-----")
if x>y and x>z:
    print("x is the largest")
if y>x and y>z:
    print("y is the largest")
if(z>x and z>y):
    print("z is the largest")
print("----or----")
ch=input("enter char:")
if(ch=='A'or ch=='a'or ch=='E'or ch=='e'or ch=='I'or ch=='i' or ch=='O'or ch=='o'or ch=='U'or ch=='u'):
    print(ch," is Vowel")
else:
    print(ch," is consonant")

print("<----Membership Opearator---->")
print("x in lst:",x in lst)
print("y in lst:",y in lst)
print("y not in lst:",y not in lst)

print("<----Identity Opearator---->")
print("x is y:",x is y)
print("x is not y:",x is not y)