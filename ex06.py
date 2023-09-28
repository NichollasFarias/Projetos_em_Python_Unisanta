import math


print("+-------------------------------------------------------------+")
print("|                          Classe SC                          |")
print("|                                                             |")
print("|   ° calcDist - calculo da distancia do ponto até a origem   |")
print("+-------------------------------------------------------------+")




class SC:
    def __init__(self, x, y):
        self.eixoX = x
        self.eixoY = y


    def __getattr__(self, atributo):
        return print("Atenção o ",atributo," não foi reconhecido\nTente Novamente")


    def __str__(self):
        return "O X é = " +str(self.eixoX)+"\nO Y é = "+str(self.eixoY)

    
    def __eq__(self,self2):
        if(self.eixoX == self2.eixoX) and (self.eixoY == self2.eixoY):
            return True
        else:
            return False

        
    def __add__(self, self2):
        self.Xm = (self.eixoX + self2.eixoX)/2
        self.Ym = (self.eixoY + self2.eixoY)/2
        return print("As cordenadas do ponto medio é( X: ", self.Xm , ", Y: ", self.Ym , ")")

    
    def __sub__(self,self2):
        distXY = math.sqrt(math.pow((self2.eixoX-self.eixoX),2)+math.pow((self2.eixoY-self.eixoY),2))
        return print("A distancia entre esses pontos é: ", distXY)


    def __truediv__(self,self2):
        coefi = (self2.eixoY-self.eixoY)/(self2.eixoX-self.eixoX)
        return print( "O coeficiente angular é: ", coefi)

    def __mul__(self,self2):
        m = (self2.eixoY-self.eixoY)/(self2.eixoX-self.eixoX)
        n = (m*self2.eixoX) - self2.eixoY
        return print("y =",m,"x +",n)
            
    def calcDist(self):
        return math.sqrt(math.pow((0-self.eixoX),2)+math.pow((0-self.eixoY),2))
        
    
