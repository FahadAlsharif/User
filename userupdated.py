import re


class user :
    def __init__(self,name,amont) -> None:
        self.name=name
        self.amont=amont
        pass
    def display(self):
        print(
            f'Name: {self.name} Balance: {self.amont}\n'
        )
        return self
    def make_withdrawal(self,lol):
        self.amont = self.amont - lol
        return self
    def transfer_money(self, other_user) :
        other_user.amont = other_user.amont + 50
        self.amont = self.amont - 50
        return self
    def deposits(self,des):
        self.amont = self.amont + des
        return self

Fahad = user("Fahad",150)
yazed = user("yazed",50)
ibra = user("ibra",100)

Fahad.display()
yazed.display()
ibra.display()
Fahad.make_withdrawal(50).transfer_money(ibra).deposits(50).deposits(50).deposits(50)
yazed.deposits(50).deposits(50).make_withdrawal(100)
Fahad.deposits(50)
ibra.deposits(50).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10)
Fahad.display()
yazed.display()
ibra.display()