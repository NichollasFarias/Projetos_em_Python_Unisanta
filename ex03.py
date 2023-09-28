print ("Ex: 01\n")

num = int(input("Digite o valor desejado: "))

for x in range(1,11):
    print(num," x ", x, " = ", num*x)



print ("\nEx: 02\n")
soma = 0

for x in range(100,201,2):
    soma += x
    
print ("A soma é: ",soma)


print ("\nEx: 03\n")

for x in range(1,21):
    enter= input("\nPressione Enter: ")
    print("\n")

    for y in range(1,11):
        print(x," x ",y," = ", x*y)
        

print ("\nEx: 04\n")

controle = ""


while(controle != "N" and controle != "n"):
    valor = 0
    fat = 1

    while(valor <= 0):
        valor = int (input("\nDigite o valor:  "))

        if(valor < 0):
            print("\nDigite Novamente!")

    for x in range(1, valor+1):
        fat = fat * x
            

    print ("O fatorial de !",valor,"é: ",fat)
    controle = input("\nQuer continuar (S/N)?: ")
        

print ("\nEx: 06\n")

na = int(input("Digite o total de alunos: "))
SM = 0
media = 0



for x in range(1,na+1):

    print("\nAluno ",x)
    n1 = int(input("Digite a nota 01: "))
    n2 = int(input("Digite a nota 02: "))
    n3 = int(input("Digite a nota 03: "))
    n4 = int(input("Digite a nota 04: "))

    media = (n1+n2+n3+n4)/4
    SM += media
    
MG = SM / na
print("\nA media da turma é: ", MG)

print ("\nEx: 07\n")

mes = int(input("Digite um numero de 1-12: "))

if(mes == 1):
    print("Mes: Janeiro Dias: 31")
elif(mes == 2):
    print("Mes: Fevereiro Dias: 28 ou 29")
elif(mes == 3):
    print("Mes: Março Dias: 31")
elif(mes == 4):
    print("Mes: Abril Dias: 30")
elif(mes == 5):
    print("Mes: Maio Dias: 31")
elif(mes == 6):
    print("Mes: Junho Dias: 30")
elif(mes == 7):
    print("Mes: Julho Dias: 31")
elif(mes == 8):
    print("Mes: Agosto Dias: 31")
elif(mes == 9):
    print("Mes: Setembro Dias: 30")
elif(mes == 10):
    print("Mes: Outubro Dias: 31")
elif(mes == 11):
    print("Mes: Novembro Dias: 30")
elif(mes == 12):
    print("Mes: Dezembro Dias: 31")
else:
    print("Mes Inexistente")

print ("\nEx: 08\n")

print("\n1- Abrir\n2- Salvar\n3- Excluir\n4- Exportar")
valor = int(input("Escolha: "))

if(valor == 1):
    print("Abrindo")
elif(valor == 2):
    print("Salvando")
elif(valor == 3):
    print("Excluindo")
elif(valor == 4):
    print("Exportando")
else:
    print("Opção Invalida")




