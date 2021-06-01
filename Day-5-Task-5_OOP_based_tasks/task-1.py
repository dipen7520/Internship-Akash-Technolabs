'''
Create a class cal1 that will calculate sum of three numbers. Create
setdata() method which has three parameters that contain numbers.
Create display() method that will calculate sum and display sum.
'''
class Cal1:
    def setdata(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        sum =self.a+self.b+self.c
        print("{}+{}+{} = {}".format(self.a,self.b,self.c,sum))


obj = Cal1()
obj.setdata(10,20,30)
obj.display()