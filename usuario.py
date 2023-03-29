class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def realizar_deposito(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


eloy = User("Eloy")
teo = User("Teo")
edson = User("Edson")

eloy.realizar_deposito(700)
eloy.realizar_deposito(100)
eloy.realizar_deposito(60)
eloy.make_withdrawl(65)
eloy.display_user_balance()

teo.realizar_deposito(2000)
teo.realizar_deposito(1000)
teo.make_withdrawl(600)
teo.make_withdrawl(200)
teo.display_user_balance()

edson.realizar_deposito(1550)
edson.make_withdrawl(2000)
edson.make_withdrawl(6000)
edson.make_withdrawl(2000)
edson.display_user_balance()


teo.transfer_money(7000, eloy)
