print ("Ex: 01\n")

base = int (input ("Entre com a base: "))
altura = int (input("Entre com a altura: "))

print ("\nA Area é igual a: ", base*altura,"m²")



print ("\nEx: 02\n")

aresta = int (input ("Entre com a aresta: "))

print ("\nA Area é igual a: ", aresta*aresta,"m²")



print ("\nEx: 03\n")

base = int (input ("Entre com a base: "))
altura = int (input("Entre com a altura: "))

print ("\nA Area é igual a: ", (base*altura)/2,"m²")



print ("\nEx: 04\n")

p1 = float (input("P1: "))
p2 = float (input("P2: "))
p3 = float (input("P3: "))
p4 = float (input("P4: "))
media = (p1+p2+p3+p4)/4

print ("\n A media do aluno é: ", media)



print ("\nEx: 05\n")

milha = int (input("Quantas milhas: "))

print ("A converção para km é: ", milha* 1.852)



print ("\nEx: 06\n")

num01 = int (input("Digite o numero 01: "))
num02 = int (input("Digite o numero 02: "))

if (num01 > num02):
    print ("O numero 01 é o maior: ", num01)

else:
    print ("O numero 02 é o maior: ", num02)




print ("\nEx: 07\n")

num01 = int (input("Digite o numero 01: "))
num02 = int (input("Digite o numero 02: "))

if (num01 < num02):
    print ("O numero 01 é o menor: ", num01)

else:
    print ("O numero 02 é o menor: ", num02)





print ("\nEx: 08\n")

base = int (input ("Entre com a base: "))
altura = int (input("Entre com a altura: "))

area = base*altura

print ("\nA Area é igual a: ", area,"m²")

if (area >= 100):
    print (" Terreno Grande")
else:
    print (" Terreno Pequeno")





print ("\nEx: 09\n")

peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso*(altura*altura)

print ("Seu IMC é igual: ",IMC)

if (IMC < 20):
    print ("Abaixo do peso")

else:
    if(20 <= IMC < 25):
        print ("Peso Ideal")
    else:
        print ("Acima do Peso")



print ("\nEx: 10\n")

ac = float (input("Digite a aceleração: "))
temp = float (input("Digite o tempo: "))
vo = float (input("Digite a Velocidade Inicial: "))

v = vo + (ac*temp)
vf = v * 3.6

print("\nA velocidade em km/h é: ", vf, "km/h")

