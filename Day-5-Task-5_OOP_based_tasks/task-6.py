'''
Create a class cal5 that will calculate area of a rectangle. Create
constructor method which has two parameters .Create calArea()
method that will calculate area of a rectangle. Create display() method
that will display area of a rectangle
'''

class Cal5:
    def __init__(self,height,width):
        self.length = lenght
        self.width = width
    
    def calArea(self):
        area = self.length * self.width
        print("Area of rectangle with length={} and width ={} is {}".format(self.length,self.width,area))

lenght =int(input("enter length:"))
width =int(input("enter width:"))

obj = Cal5(lenght,width)
obj.calArea()