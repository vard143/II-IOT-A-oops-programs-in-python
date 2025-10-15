class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner         #public
        self__balance=balance    #private

    def bygetter(self):
        return self__balance
    def bysetter (self,amount):
        if amount>=0:
            self__balance=amount

        else:
            print("invalid amount")

obj=BankAccount("vardhan",22000)
print(obj.bygetter())
obj.bysetter(54000)
print(obj.bygetter())
