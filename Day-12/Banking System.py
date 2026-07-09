class Account:
    def __init__(self,balance,acc_no):
        self.balance= balance
        self.acc_no= acc_no
    def debit(self,withdrawl_amt):
        if self.balance>=withdrawl_amt:
            if(withdrawl_amt>0):
                self.balance=self.balance-withdrawl_amt
                print(f"Action: Withdrawl, Account No: {self.acc_no}, Withdrwal amt: Rs.{withdrawl_amt}")
            else:
                print(f"Invalid Transaction, Trying to debit: Rs.{withdrawl_amt}")
        else:
            print("Not Sufficient money to withdraw")
    def credit(self,credit_amt):
        if credit_amt>0:
            self.balance=self.balance+credit_amt
            print(f"Action: Credit, Account No: {self.acc_no}, Credit amt: Rs.{credit_amt}")
        else:
            print(f"Invalid Transaction, Trying to credit: Rs.{credit_amt}")
    def print_bal(self):
        print(f"Action: Check Balance, Account No: {self.acc_no}, Balance: Rs.{self.balance}")
        
p1=Account(20000,68521011)
p1.print_bal()
p1.credit(5000)
p1.debit(2000)
p1.print_bal()
