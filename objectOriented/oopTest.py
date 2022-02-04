class Bank:
    ''' bank class'''
    accholderName=""
    balance=0
    COUNT=0

   def __init__(self,name=None,balance=None):
   if(name is not None):
        self.accholderName=name
    if(balance is not None):
        self.balance=balance
    Bank.COUNT+=1

    def deposit(self,amount):
        self.balance=self.balance+amount


    def withdraw(self,amount):
        self.balance = self.balance-amount

    @staticmethod
    def TotalAccounts():
        print("Total Accounts in Bank ={0}".format(Bank.COUNT))

    def __del__(self):
       print('{0} is being destroyed!'.format(self.accholderName))
       Bank.COUNT-=1

class Savings(Bank):
    '''Rep[ersens child class'''
    isSalaryAccount=False

    def __str__(self):
        return super.__str__()+" isSalaryAccount: "+ str(self.isSalaryAccount)

    def __init__(self,name,balance,isSalAcc):
        super().__init__(name,balance)
'''
b = Bank()
setattr(b,'accholderName','Krunal')
print(getattr(b,'accholderName'),'',getattr(b,'balance'))

b.deposit(5000)
print(getattr(b,'accholderName'),'',getattr(b,'balance'))

b.withdraw(3000)
print(getattr(b,'accholderName'),'',getattr(b,'balance'))

print(b.__doc__)
'''

b1 = Bank("Mike")
b2= Bank("John",5000)
print(Bank.TotalAccounts())

del b1
del b2
print(Bank.TotalAccounts())

s= Savings("Martin",5000,True)
print(getattr(s,'accholderName'),'',getattr(s,'balance'),'',getattr(s,'isSalaryAccount'))
print(Bank.TotalAccounts())
print(s)


