from module import fact
def function():
    print("hello")
def functionarg(arg):
    print(arg)
def returnfun():
    a=10
    b=20
    return "a+b={}".format(a+b)

def mreturn():
    name = "LDCE"
    depart = "IT(7th sem)"
    return name,depart

def default(a=10,b=20):
    return a+b

def keyargs(a,b):
    return a-b

def varlength(*num):
    obj=[]
    for i in num:
        obj.append(i)
    return obj
def varlengthk(**keyargs):
    dis = {}
    for key,val in keyargs.items():
        dis[key] = val
    return dis
def scope():
    x=10
    print("Value inside function : ",x)

print("----simple function----")
function()

print("----function with arguments----")
functionarg("Hello World")

print("----function with return----")
print(returnfun())

print("---function with multiple return---")
name,depart = mreturn()
print("College = {}".format(name))
print("Department = {}".format(depart))

print("---Default arguments---")
print("default() :",default())
print("default(4,5) :",default(4,5))

print("---Keyword arguments---")
print("keyargs(a=10,b=20)",keyargs(a=10,b=20))
print("keyargs(b=10,a=20)",keyargs(b=10,a=20))

print("---Var-length(non-keyword) arguments---")
print("varlength(10,20) : ",varlength(10,20))
print("varlength(10,20,30) : ",varlength(10,20,30))
print("varlength(10,20,30,40) : ",varlength(10,20,30,40))

print("---Var-length(keyword) arguments---")
print('varlengthk(car="BMW",price=2500000) :::',varlengthk(car="BMW",price=2500000))
print('varlengthk(car="BMW",price=2500000,country="india") :::',varlengthk(car="BMW",price=2500000,country="india"))

print('----Scope of Variable----')
x=20
scope()
print("value outside function:",x)

print('----Module Function----')
print(fact(5))

print()
print()
print()