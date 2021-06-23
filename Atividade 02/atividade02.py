class Calculadora:
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        return self.numero1 + self.numero2

    def sub(self):
        return self.numero1 - self.numero2

    def mult(self):
        return self.numero1 * self.numero2

    def div(self):
        return self.numero1 / self.numero2
        

    

p1 = Calculadora(2, 3)
p1.soma()