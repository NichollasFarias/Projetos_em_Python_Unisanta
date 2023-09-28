import sqlite3

conexao = sqlite3.connect('Futebol.db')
cursor = conexao.cursor()

conexao.execute('CREATE TABLE IF NOT EXISTS notas(ID integer PRIMARY KEY AUTOINCREMENT, Clube text, Pontos integer, Vitorias integer, Empates integer, Jogos integer, Gols_Marcados integer, Gols_Sofridos integer, Saldo_de_Gols integer, Aproveitamento decimal)')


Sair = True

while(Sair):
    print("+--------------------------+")
    print("|           Menu           |")
    print("|                          |")
    print("|       1- Inserir         |")
    print("|    2- Pesquisa Club      |")
    print("|      3- Pontuação        |")
    print("|    4- Aproveitamento     |")
    print("|        5- Sair           |")
    print("|                          |")
    print("+--------------------------+")

    op = int(input("Escolha: "))
    print("\n\n")

    if(op == 1):
        
        pontos = 0
        nome = input("Entre com o nome do Clube: ")
        vitorias = int(input("Total de Vitorias: "))
        empates = int(input("Total de Empates: "))
        jogos = int(input("Total de Jogos: "))
        golM = int(input("Total de Gols Marcados: "))
        golS = int(input("Total de Gols Sofridos: "))
        for x in range(vitorias):
            pontos+=3
        for x in range(empates):
            pontos+=1
        SaldoGol = golM - golS
        Aprove = (pontos/(jogos*3))*100
        conexao.execute('INSERT INTO notas VALUES(NULL,?,?,?,?,?,?,?,?,?)', (nome,pontos,vitorias,empates,jogos,golM,golS,SaldoGol,Aprove))
        conexao.commit()
        print("\n\n")

    elif(op == 2):

        opnome = input("Digite o Nome do Clube: ")

        cursor.execute('SELECT * FROM notas WHERE Clube= :name', {"name": opnome})
        re = cursor.fetchone()
        print("\n\n")
        print("Nome do Clube: ", re[1])
        print("Pontos: ", re[2])
        print("Vitorias: ", re[3])
        print("Empates: ", re[4])
        print("Jogos: ", re[5])
        print("Gols Marcados: ", re[6])
        print("Gols Sofridos: ", re[7])
        print("Saldo de Gols: ", re[8])
        print("Aproveitamento: ", re[9])
        print("\n\n")
        conexao.commit()
    
    elif(op == 3):

        opponto = int(input("Digite a Pontuação: "))

        cursor.execute('SELECT * FROM notas WHERE Pontos= :ponto', {"ponto": opponto})
        re = cursor.fetchall()
        for row in re:
            
            print("\n\n")
            print("Nome do Clube: ", row[1])
            print("Pontos: ", row[2])
            print("Vitorias: ", row[3])
            print("Empates: ", row[4])
            print("Jogos: ", row[5])
            print("Gols Marcados: ", row[6])
            print("Gols Sofridos: ", row[7])
            print("Saldo de Gols: ", row[8])
            print("Aproveitamento: ", row[9])
            print("\n\n")

    elif(op == 4):

        opaprov = float(input("Digite a Pontuação: "))

        cursor.execute('SELECT * FROM notas WHERE Aproveitamento= :aprov', {"aprov": opaprov})
        re = cursor.fetchall()
        for row in re:
            
            print("\n\n")
            print("Nome do Clube: ", row[1])
            print("Pontos: ", row[2])
            print("Vitorias: ", row[3])
            print("Empates: ", row[4])
            print("Jogos: ", row[5])
            print("Gols Marcados: ", row[6])
            print("Gols Sofridos: ", row[7])
            print("Saldo de Gols: ", row[8])
            print("Aproveitamento: ", row[9])
            print("\n\n")

        
    elif(op == 5):
        Sair = False
    else:
        print("Opção invalida, Tente Novamente")
