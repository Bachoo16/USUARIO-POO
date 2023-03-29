class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        

    def hacer_deposito(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


eloy = User("Eloy")
teo = User("Teo")
edson = User("Edson")

eloy.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).make_withdrawl(45).display_user_balance()

teo.hacer_deposito(1000).hacer_deposito(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()

edson.hacer_deposito(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()


teo.transfer_money(400, eloy)