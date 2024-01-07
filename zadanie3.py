# 3
class Alkoholik:
    def __init__(self, _bimber: str, _whisky: str, _gin: str) -> None:
        self.bimber = _bimber
        self.whisky = _whisky
        self.gin = _gin
                
    def Bimber(self):
        print("kocham bimberek")

    def Whiskey():
        print("kocham też whisky")

    def Gin():
        print("a także gin:)")
        
    def inf2(self):
        print(self.bimber)
        print(self.whisky)
        print(self.gin)

a = Alkoholik("bimber", "whisky", "gin")
a.inf2()    