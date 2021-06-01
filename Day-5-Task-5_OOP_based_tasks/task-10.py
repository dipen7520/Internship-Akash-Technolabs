'''
Create a arith class. The class should have a parameterized constructor
and methods to add, subtract and multiply two numbers and to return
the answers.
'''

class Arith:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def sum1(self):
        return (self.a + self.b)
    def sub2(self):
        return (self.a - self.b)
    def mul3(self):
        return (self.a * self.b)


num1 = int(input("enter a: "))
num2 = int(input("enter b: "))

obj = Arith(num1,num2)


print("{} + {} = {} ".format(num1,num2,obj.sum1()))
print("{} - {} = {} ".format(num1,num2,obj.sub2()))
print("{} * {} = {} ".format(num1,num2,obj.mul3()))