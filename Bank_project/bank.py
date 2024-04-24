from datetime import date as d
from pandas import DataFrame
from collections import defaultdict
class bank:
    bank_name = "IOB"
    IFFC = "176879809jjk"
    Branch = "Vadapalani"
    def __init__(self, name,ph,age,ac,bal):
        self.name = name
        self.age = age
        self.ac = ac
        self.ph = ph
        self.bal = bal
        self.st = defaultdict(list)
        
    def detail(self):
        print(f"bank name : {self.bank_name}\n"
              f"IFSC CODE : {self.IFFC}\n"
              f"BRANCH : {self.bank_name}\n"
              f"NAME : {self.name}\n"
              f"AGE : {self.age}\n"
              f"PH : {self.ph}\n"
              f"ACCOUNT NUMBER : {self.ac}\n"
              f"AVALABLE BALANCE : {self.bal}")
    
    def deposit(self,amt):
        if amt > 0:
            self.bal += amt
            print(f"Your account {amt}RS was cretited successfully\n"
                  f"Total Bal : {self.bal}")
            self.st["des"] += ["Deposit"]
            self.st["Date"] += [d.today()]
            self.st["CR"] += [amt]
            self.st["DR"] += ['-']
            self.st["TOTAL BALANCE"] += [self.bal]
            
    def Withdraw(self,amt):
        if amt <= self.bal:
            self.bal -= amt
            print(f"Your account {amt}RS was withdraw successfully\n"
                  f"Total Bal : {self.bal}")
            self.st["des"] += ["Withdraw"]
            self.st["Date"] += [d.today()]
            self.st["CR"] += ['-']
            self.st["DR"] += [amt]
            self.st["TOTAL BALANCE"] += [self.bal]
    
    def transfer(self,cus,amt):
        if amt <= self.bal:
            self.bal -= amt
            print(f"Your account {amt}RS was Transfer successfully\n"
                  f"Total Bal : {self.bal}")
            cus.bal += amt
            self.st["des"] += [f"Transfer to {cus.name}"]
            self.st["Date"] += [d.today()]
            self.st["CR"] += ['-']
            self.st["DR"] += [amt]
            self.st["TOTAL BALANCE"] += [self.bal]
            cus.st["des"] += [f"Received from {self.name}"]
            cus.st["Date"] += [d.today()]
            cus.st["CR"] += [amt]
            cus.st["DR"] += ['-']
            cus.st["TOTAL BALANCE"] += [self.bal]
            
    def interest(self,rate = 5.4):
        iamt = self.bal*(rate/100)
        self.bal += iamt
        print(f"Your account got credited {iamt}RS as interest \n"
              f"Total Balance : {self.bal}")
        self.st["des"] += ["intersest"]
        self.st["Date"] += [d.today()]
        self.st["CR"] += [iamt]
        self.st["DR"] += ['-']
        self.st["TOTAL BALANCE"] += [self.bal]
    
    def statement(self):
        df = DataFrame(self.st)
        print(df)
        
    
murugan = bank('Murugan',9083873872,22,8374897123,1500)
kumar = bank('KUMAR',88798977,22,7876776786,2500)
siva = bank('Sivakarthikeyan',8389738274,12,89984729823,500)
kumar.transfer(siva,2000)
print(kumar.bal)
print(siva.bal)
kumar.deposit(5000)
siva.deposit(300)
kumar.statement()
siva.statement()