'''
Create a class called scheme with scheme_id,
scheme_name,outgoing_rate, and message_charge. Derive customer
class form scheme and include cust_id, name and mobile_no
data.Define necessary functions to read and display data
'''

class Scheme:
    scheme_id = 0
    scheme_name = ""
    outgoing_rate = 0
    message_charge = 0
    def __init__(self,id,name,rate,charge):
        self.scheme_id = id
        self.scheme_name = name
        self.outgoing_rate = rate
        self.message_charge = charge
    
    def display(self): 
        print("Scheme id      : ",self.scheme_id)
        print("Scheme name    : ",self.scheme_name)
        print("Outgoing rate  : ",self.outgoing_rate)
        print("Message Charge : ",self.message_charge)



class Customer(Scheme):
    def __init__(self,id,name,mobile):
        self.cust_id = id
        self.cust_name = name
        self.mobile_no = mobile 

    def dis(self):
        print("Customer id : ",self.cust_id)
        print("Customer name : ",self.cust_name)
        print("Customer mobile : ",self.mobile_no)


obj1 = Scheme(1,"ABC",20.4,10000) 
obj2 = Customer(10,"PQR",1234569878)
obj1.display()
obj2.dis()