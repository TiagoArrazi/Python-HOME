class Account:

   def __init__(self, accountName, accountNumber, cashAmount = 0):

       self.accountName = accountName
       self.accountNumber = accountNumber
       self.cashAmount = cashAmount

   def showAccountName(self):

       print('The owner of account ' + str(self.accountNumber) + ' is ' + str(self.accountName))

   def showAccountNumber(self):

       print(self.accountName + '\'s account number is ' + self.accountNumber)

   def showAccountCash(self):
       
       print('The total amount of money in the account ' + str(self.accountNumber) + ' is $' + str(self.cashAmount) + '\n')

   def showAccountData(self):

        print(self.accountName)
        print(self.accountNumber)
        print(self.cashAmount)
       

   def depositInAccount(self, depositAmount):
       
       self.cashAmount += depositAmount
       print('$' + str(depositAmount) + ' has been deposited in account of number ' + str(self.accountNumber))
       self.showAccountCash()

   def withdrawFromAccount(self, withdrawAmount):
       
       if self.cashAmount > 0 and self.cashAmount > withdrawAmount:
           
           self.cashAmount -= withdrawAmount
           print('$' + str(withdrawAmount) + ' has been withdrawn from account of number ' + str(self.accountNumber))
           self.showAccountCash()
           
       else:

           print('Not enough cash!' + '\n')

a = Account('Tiago', '2221603-1')

a.depositInAccount(50)
a.withdrawFromAccount(10)



