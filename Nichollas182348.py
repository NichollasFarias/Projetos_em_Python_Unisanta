#Nome: Nichollas de Farias Leonides dos Santos
#RA: 182348

class Data:

    def __init__(self,data = "01/01/2000"):

        lista = data.split('/')

        
        self.dia = int(lista[0])
        self.mes = int(lista[1])
        self.ano = int(lista[2])

        if(self.dia > 31):
            self.dia = 1
        if(self.mes > 12):
            self.mes = 1
        if(self.ano < 2000) or (ano > 2999):
            self.ano = 2000
            
        

    def __getattr__(self, atributo):
        

    def __eq__(self,self2):
        if(self.dia == self2.dia) and (self.mes == self2.mes) and (self.ano == self2.ano):
            return True
        else:
            return False

    def __gt__(self,self2):
        if(self.ano > self2.ano):
            return True
        else:
            return False

    def __sub__(self,self2):
        if(self.ano > self2.ano):
            DifeAno = self.ano - self2.ano
            i = self2.ano
            for x in range(DifeAno):
                if(i % 4 == 0):
                    diano +=366
                else:
                    diano += 365
                i++
        else:
            DifeAno = self2.ano - self.ano
            i = self.ano
            for x in range(DifeAno):
                if(i % 4 == 0):
                    diano +=366
                else:
                    diano += 365
                i++

        return print("O total de Dias entre é: ",diano)

    def verBissexto(self):
        bissexto = self.ano % 4
        if(bissexto == 0):
            return True
        else:
            return False

    def difDias(self):
        DifeAno = self.ano - 2000
        i = 2000
        for x in range(DifeAno):
            if(i % 4 == 0):
                diano +=366
            else:
                diano += 365
            i++

        return print("O total de Dias entre é :", diano)
    

    
