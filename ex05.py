import math
print ("Ex: 01\n")

def media():
    n1 = int(input("Entre com o valor da nota 01: "))
    n2 = int(input("Entre com o valor da nota 02: "))
    n3 = int(input("Entre com o valor da nota 03: "))
    R = (n1+n2+n3)/3;
    print("A media é igual: ",R)

media()

print ("\nEx: 03\n")

def Menu():
    print("+---------------------------------+")
    print("|           Menu                  |")
    print("|                                 |")
    print("|   1 - Valor 10                  |")
    print("|   2 - Valor 20                  |")
    print("|   3 - Valor 30                  |")
    print("|   4 - Valor 40                  |")
    print("|   5 - Valor 50                  |")
    print("|                                 |")
    print("+---------------------------------+")

    op = int(input("Entre com a opção desejada: "))

    if(op == 1):
        print("10")
    
    elif(op == 2):
        print("20")

    elif(op == 3):
        print("30")

    elif(op == 4):
        print("40")

    elif(op == 5):
        print("50")

    else:
        print("Opção invalida")
    

Menu()


print ("\nEx: 04 e 05\n")

print("Use a função: Polar(X,Y)\n")
print("Use a função: Retan(Z,O)\n")


def Polar(x,y):
    """Entra com valores X+jY """
    z = pow(x,2)+pow(y,2)
    Z = math.sqrt(z) 
    o = y/x
    O = math.degrees(math.atan(o))
    print(Z,"|",O)

def Retan(Z,O):
    """ o "O" é o angulo e o "Z" é o primeiro numero"""
    X = Z*math.cos(math.radians(O))
    
    Y = Z*math.sin(math.radians(O))
    
    print(X,"+j",Y)

