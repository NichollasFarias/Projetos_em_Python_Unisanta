print ("Ex: 01\n")

num01 = int(input("Digite o primeiro valor: "))
num02 = int(input("Digite o segundo valor: "))
while(num02 < num01):
    print ("\nERROR")
    num02 = int(input("Digite novamente o segundo valor: "))
print ("Confirmado")


print ("\nEx: 02\n")

controle = ""

while(controle != "fim" and controle != "FIM"):
    sexo = input("\nDigite seu sexo (F/M): ")
    if(sexo == "F" or sexo == "M"):
        print("\nSexo confirmado\n")
    else:
        print("\nSexo não confirmado, Digite novamente\n")
    controle = input("Digite FIM/fim para ir para proximo ex, ou enter para continuar: ")
    




print ("\nEx: 03\n")

passe = True
cont = 1
while (passe == True):
    num = int(input("Digite um numero positivo: "))
    if(num < 0):
        print("Valor menor que 0, digite novamente")
    else:
        passe = False
        
while (cont <= 10):
    r = num * cont
    print ("\n",num,"x",cont,"=",r)
    cont = cont + 1




print ("\nEx: 04\n")
cont = 1
soma = 1
while(cont <= 100):
    r = soma
    soma = soma + cont
    print ("\n",r,"+",cont,"=",soma)
    cont = cont + 1

print ("\nEx: 05\n")
maior = 0
soma = 0
cont = 1

while(cont <= 10):
    num = int(input("Digite um numero: "))

    if(num > maior):
        maior = num
        
    soma = soma + num
    cont = cont + 1

media = soma / 10

print("\nO maior valor: ", maior,"\nA soma deles: ", soma,"\nA media: ", media)

print ("\nEx: 06\n")
lista = []
cont = 1

while(cont <= 10):
    valor = int(input("Digite um numero: "))
    lista.append(int(valor))
    cont += 1
    

print(lista)
multi = int(input("Digite uma constante para multiplicação da lista: "))
n = 0
R = 0

while(n <= 9):
    R = multi * lista[n]
    lista[n] = R
    n += 1

print(lista)



print ("\nEx: 07\n")

lista = []
cont = 1

while(cont <= 20):
    valor = int(input("Digite um numero: "))
    lista.append(int(valor))
    cont += 1
    
print (lista)
lista.sort()
print (lista)


print ("\nEx: 08\n")

lista = []
cont = 1

while(cont <= 20):
    valor = int(input("Digite um numero: "))
    lista.append(int(valor))
    cont += 1
    
print (lista)
lista.sort(reverse=True)
print (lista)



print ("\nEx: 09\n")

lista = []
cont = 1

while(cont <= 10):
    valor = int(input("Digite um numero: "))
    lista.append(int(valor))
    cont += 1

print ("\nO maior valor: ",max(lista))
print ("O menor valor: ",min(lista))
print ("A soma é: ",sum(lista))
print ("E sua media é: ",sum(lista)/10)


