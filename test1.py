data = input("Digite a data: ")

lista = data.split("/")

dia = int(lista[0])
mes = int(lista[1])
ano = int(lista[2])

if(dia > 31):
    dia = 1
if(mes > 12):
    mes = 1
if(ano < 2000) or (ano > 2999):
    ano = 2000
    
print(dia)
print(mes)
print(ano)
