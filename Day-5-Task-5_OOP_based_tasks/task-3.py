'''Create a class cal3 that will calculate simple interest. Create
constructor method which has three parameters .Create calInterest()
method that will calculate Interest . Create display() method that will
display Interest.'''

class Cal3:
    p=0
    r=0
    n=0
    def __init__(self,p,r,n):
        self.p = p
        self.r = r
        self.n = n
    def calInterest(self):
        s_interest = (self.p*self.r*self.n)/100

        print('for p={},r={},n={} simple interest = {:.2f}'.format(self.p,self.r,self.n,s_interest))
    

p  = int(input("enter p:"))
r  = float(input("enter r:"))
n  = int(input("enter n:")) 
obj = Cal3(p,r,n)
obj.calInterest()