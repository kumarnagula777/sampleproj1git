class Cust:
    """cust app"""
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def deposit(self,damt):
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
c1=Cust("ravana","srilanka",1001,100000.00)
print(c1)
c1.deposit(40000.00)
c1.withdraw(60000.00)
c1.display()
c2=Cust("sita","india",1002,1000.00)
print(c2)
c2.deposit(4000.00)
c2.withdraw(12000.00)
c2.display()

c3=Cust("sita","india",1002,1000.00)
print(c3)
c3.deposit(4000.00)
c3.withdraw(12000.00)
c3.display()