"""#classes and objects
class Car:
    color = "blue"
    brand = "tata"

car1 = Car()    
print(car1.color)
print(car1.brand)

#__init__ functon:

class Student:
    college_name = "ABC College"

    #default constructor:
    def __init__(self):
         pass

    #parameter constructor:
    def __init__(self, full_name,marks):
        self.name = full_name
        self.marks = marks
        print("adding new student in database:")

    def Welcome(self):
        print("Welcome student,",self.name)   

    def get_marks(self):
        return self.marks 

s1 = Student("Akhil",98)
print(s1.name, "|", s1.marks)
print(s1.college_name)
s1.Welcome()
print(s1.get_marks())

s2 = Student("Harshith",99)
print(s2.name,"|",s2.marks)
print(s2.college_name)
s2.Welcome()
print(s2.get_marks())"""

#Abstraction

class Car:
    def __init__(self):
        self.acc = False   #not showed or hided
        self.brk = False   #not showed or hided
        self.clucth = False   #not showed or hided

    def Start(self):
        self.clucth = True   #not showed or hided
        self.acc = True   #not showed or hided
        print("Car started..")

car1 = Car()
car1.Start()


#class account 

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount) :
        self.balance += amount
        print("Rs.",amount,"was debited") 
        print("total balance",self.get_balance()) 

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(1000,12345)
acc1.debit(1000)                
acc1.credit(500)




