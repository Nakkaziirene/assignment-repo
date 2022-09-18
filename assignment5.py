
class BankAccount:
    def __init__(self, account_number: str, balance: float, owner: str, type: str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
        self.transactions = []

    def __repr__(self) -> str:
        return "Account Number is: {} \nBalance is: {} \nOwner: {} \nAccount Type is: {}".format(self.account_number, self.balance, self.owner, self.type)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accts = []
    
    def __repr__(self):
        return "Bank Name is: {}".format(self.name)

    def add_Bank_account(self, bankAc):
        self.accts.append(bankAc)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.accts = []

    def __repr__(self) -> str:
        return "Customer Name is: {}".format(self.name)
    
    def add_bank_account(self, bankAcct):
        self.accounts.append(bankAcct)

class Transactions:
    def __init__(self, account, amount: float, type: str, balancebefore: float):
        self.account = account
        self.amount = amount
        self.type = type
        self.balancebefore = balancebefore

    def processTransaction(self):
        if self.type == "deposit":
            #newbalance = self.previousbalance + self.amount
            return "Balance after Deposit is: {}".format((float(self.balancebefore + self.amount)))
        
        elif self.type == "withdrawal":
            return "Balance after Withdrawal is: {}".format((float(self.balancebefore - self.amount)))
    

if __name__ == '__main__':

    bank_name = input("Enter Bank Name: ")
    customer_name = input("Enter customer name ")
    initial_dep = float(input("Enter initial deposit "))
    acctno = input("Enter account number ")
    type = input("Enter account type savings or current ")

    #create a new bank object
    New_Bank_Object = Bank(bank_name)

    #create a new customer object
    New_Customer_Object = Customer(customer_name)

    #create a new bank account object
    New_Bank_Acct_Object = BankAccount(acctno, initial_dep, customer_name, type)

    #print the bank obj
    print(New_Bank_Object)

    #print the cust obj
    print(New_Customer_Object)

    #print the bankacct obj
    print(New_Bank_Acct_Object)

    insidemenu =int(input("Input 1 to deposit, Input 2 to withdraw "))

    if insidemenu ==1:
        amount =int(input("Input amount to deposit "))
        #get balance before posting transaction
        #craete new transaction obj
        newTransObject = Transactions(acctno, amount, "deposit", New_Bank_Acct_Object.balance)
        print(newTransObject.processTransaction())

    elif insidemenu ==2:
        #get balance before posting transaction
        amount =int(input("Input amount to withdraw "))
        #create new transaction obj
        newTransObject = Transactions(acctno, amount, "withdrawal", New_Bank_Acct_Object.balance)
        print(newTransObject.processTransaction())

    else:
        print("invalid output")
