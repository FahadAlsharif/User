class user :
    def __init__(self,name,amont) -> None:
        self.name=name
        self.amont=amont
        pass
    def display(self):
        print(
            f'Name: {self.name} Balance: {self.amont}\n'
        )
        return
    def make_withdrawal(self,lol):
        self.amont = self.amont - lol
        return
    def transfer_money(self, other_user) :
        other_user.amont = other_user.amont + 50
        self.amont = self.amont - 50
    def deposits(self,des):
        self.amont = self.amont + des

Fahad = user("Fahad",150)
yazed = user("yazed",50)
ibra = user("ibra",100)

Fahad.display()
yazed.display()
ibra.display()
Fahad.make_withdrawal(50)
Fahad.transfer_money(ibra)
Fahad.deposits(50)
Fahad.deposits(50)
Fahad.deposits(50)
yazed.deposits(50)
yazed.deposits(50)
yazed.make_withdrawal(100)
Fahad.deposits(50)
ibra.deposits(50)
ibra.make_withdrawal(10)
ibra.make_withdrawal(10)
ibra.make_withdrawal(10)
Fahad.display()
yazed.display()
ibra.display()