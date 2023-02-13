import pymysql
import time
import locale

login = str
password = str
choice_str = str

#Etapa de login e criação de cadastro
def wellcome():
    global choice_str
    print("""        ###########################################\n
        Seja bem vindo ao sistema de Banco Patrick!\n
        ###########################################\n\n
        1 - Login
        2 - Criar Cadastro
        3 - Sair
    """)

    choice_str = input("        O que deseja? ")
    menuChoices()

def menuChoices():
    global choice_str
    try:
        choice = int(choice_str)
        if choice == 1:
            menuLogin()
        elif choice == 2:
            signUp()
        elif choice == 3:
            print("        Obrigado! Volte sempre.")
            time.sleep(2)
            exit()
        else:
            print("\n\n"," "*7,"Opção inválida, tente novamente.","\n"," "*7,"#"*42,"\n\n")
            time.sleep(1)
            wellcome()
    except:
        print("\n\n"," "*7,"Opção inválida, tente novamente.","\n"," "*7,"#"*42,"\n\n")
        time.sleep(2)
        wellcome()

def menuLogin():
    #criando conexão com o banco
    conexao = pymysql.connect(host='localhost', user='root', password='', database='banco')
    cursor = conexao.cursor()

    global login
    global password
    print("""\n\n        ###########################################
    \t\t\t\t  SESSÃO DE LOGIN
        ###########################################""")
    searchLogin = input("        Login: ")
    cursor.execute(f"SELECT login FROM clientes WHERE login='{searchLogin}'")
    login_cl = cursor.fetchall()
    searchPassword = input("        Senha: ")
    try:
        if searchLogin == login_cl[0][0]:
            login = login_cl
            cursor.execute(f"SELECT senha FROM clientes WHERE senha='{searchPassword}'")
            password_cl = cursor.fetchall()
            if searchPassword == password_cl[0][0]:
                password = password_cl
                print(" "*7,"_"*21)
                print(" "*7,"|   Conectando...   |")
                print(" "*7,"_"*21)
                time.sleep(1)
                print("        ...         ")
                time.sleep(1)
                print("        .......       ")
                time.sleep(1)
                print("        ..........     ")
                time.sleep(2)
                clientLobby()
            else:
                time.sleep(1)
                print("\n"," "*6,"_"*21,"\n"," "*6,"|  Senha inválida.  |\n"," "*6,"-"*21,"\n")
                time.sleep(2)
                wellcome()
        else:
            time.sleep(1)
            print("\n", " " * 6, "_" * 21, "\n", " " * 6, "|  Senha inválida.  |\n", " " * 6, "-" * 21, "\n")
            time.sleep(2)
            wellcome()
    except:
        time.sleep(1)
        print("\n"," "*6,"_"*21,"\n"," "*6,"|  Login inválido.  |\n"," "*6,"-"*21,"\n")
        time.sleep(2)
        wellcome()

    else:
        time.sleep(1)
        print("\n"," "*6,"_"*21,"\n"," "*6,"|  Login inválido.  |\n"," "*6,"-"*21,"\n")
        time.sleep(2)
        wellcome()

def signUp():
    #fazendo a conexão com o banco de dados
    conexao = pymysql.connect(host='localhost',user='root',password='',database='banco')
    cursor = conexao.cursor()

    print("""\n\n        ###########################################
    \t\t\t    SESSÃO DE CADASTRO
        ###########################################""")
    try:
        newLogin = input("        Digite um novo Login: ")
        newPass = input("        Digite uma Senha para cadastro: ")
        newName = input("        Nome: ")
        newCPF = input("        CPF: ")
        sale = float(0)
        cli_sql = "INSERT INTO clientes(login, senha, nome, cpf, saldo) VALUES (%s, %s, %s, %s, %s)"
        new_account = (f"{newLogin}", f"{newPass}", f"{newName}", f"{newCPF}", f"{sale}")
        cursor.execute(cli_sql, new_account)
        conexao.commit()

    except:

        print("""\n\n        Login já existente, tente novamente.
        ###########################################\n\n""")
        time.sleep(2)
        wellcome()

    else:

        print("""\n\n        Cadastro criado com sucesso!
        ##############################################\n\n""")
        time.sleep(3)
        wellcome()

#Area do Cliente
def clientLobby():
    #Fazendo conexão com o banco de dados
    conexao = pymysql.connect(host='localhost', user='root', password='', database='banco')
    cursor = conexao.cursor()
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    global login
    log_cli = login[0][0]

    cursor.execute(f"SELECT conta FROM clientes WHERE login='{log_cli}'")
    account_CLI = cursor.fetchall()
    account = account_CLI[0][0]

    cursor.execute(f"SELECT nome FROM clientes WHERE login='{log_cli}'")
    name_CLI = cursor.fetchall()
    name = name_CLI[0][0]

    cursor.execute(f"SELECT saldo FROM clientes WHERE login='{log_cli}'")
    sale_CLI = cursor.fetchall()
    sale_str = sale_CLI[0][0]
    sale = float(sale_str)

    cursor.execute(f"SELECT cpf FROM clientes WHERE login='{log_cli}'")
    cpf_CLI = cursor.fetchall()
    cpf_str = cpf_CLI[0][0]
    cpf = float(cpf_str)

    print("\n\n"," "*6,"_"*91,"\n\t\t\t\t\t\t\t", " "*7, f"SEJA BEM VINDO(a) {name}!!","\n"," "*6,"_"*91,"\n\n")
    time.sleep(1)
    print(" "*7,"#"*91,"\n")
    print(" "*7,f"Nome: {name}\t\t\t\t\tConta: {account}\t\t\t\tSaldo:",locale.currency(sale),"\n")
    print(" "*7,"#"*91,"\n")

    print(" "*7,"|   1 - Depositar\t\t|\t 2 - Transferir\t\t|\t 3 - Cadastro\t\t|\t 4 - Sair     |","\n\n"," "*6,"#"*91)

    choice_str = input("        Opção: ")
    try:
        choice = int(choice_str)
        if choice == 1:
            result = float
            deposit_value = float(input("        Valor de depósito: "))
            result = sale+deposit_value
            cli_deposit = f"UPDATE clientes SET saldo = '{result}' WHERE login = '{log_cli}'"
            cursor.execute(cli_deposit)
            conexao.commit()
            time.sleep(1)

            print("\n", " " * 6, "_" * 50)
            print(" " * 7, f"|   Valor de",locale.currency(deposit_value),"depositado com sucesso!!   |")
            print(" " * 7, "-" * 50, "\n")

            time.sleep(2)
            clientLobby()

        elif choice == 2:
            print("\n"," "*6,"DIGITE VALOR 0 PARA CANCELAR AÇÃO\n")
            time.sleep(1)
            transfer = float(input("        Valor de transferência: "))

            while transfer != 0:
                accountTransfer = int(input("        Numero da Conta para transferência: "))
                cursor.execute(f"SELECT conta FROM clientes WHERE conta = '{accountTransfer}'")
                accountDestiny = cursor.fetchall()

                if accountTransfer == accountDestiny[0][0]:
                    accountD = int(accountDestiny[0][0])
                    cursor.execute(f"SELECT nome FROM clientes WHERE conta = '{accountTransfer}'")
                    clientDestiny = cursor.fetchall()
                    clientD = clientDestiny[0][0]

                    cursor.execute(f"SELECT saldo FROM clientes WHERE conta = '{accountTransfer}'")
                    saleDestiny = cursor.fetchall()
                    saleD = saleDestiny[0][0]

                    print(" "*7,f"NOME: {clientD}\n"," "*6,f"CONTA: {accountD}\n\n")
                    conf = input("        CONFIRMAR TRANSFERENCIA ( 1 - SIM/ 2 - CANCELAR )? ")
                    conF = int(conf)

                    if conF == 1:

                        resTransfer = sale - transfer
                        cli_newsale = f"UPDATE clientes SET saldo = '{resTransfer}' WHERE login = '{log_cli}'"
                        cursor.execute(cli_newsale)
                        conexao.commit()

                        new_saleD = float(saleD)
                        resultDestiny = new_saleD + transfer
                        destiny_sale = f"UPDATE clientes SET saldo = '{resultDestiny}' WHERE conta = '{accountD}'"
                        cursor.execute(destiny_sale)
                        conexao.commit()

                        print("\n"," "*6,"_"*50)
                        print(" " * 7,f"|   Valor de", locale.currency(transfer),"transferido com sucesso!!   |")
                        print(" " * 7, "-" * 50, "\n")

                        time.sleep(2)
                        clientLobby()

                    elif conF == 2:
                        print(" " * 7, "AÇÃO CANCELADA.")
                        time.sleep(1)
                        clientLobby()

                    else:
                        print(" " * 7, "OPÇÃO INVÁLIDA.")
                        time.sleep(1)
                        clientLobby()

                else:
                    print("\n"," "*5,"_"*43,"\n"," "*5,"|  Conta não encontrada. Tente novamente  |","\n"," "*5,"-"*43)
                    time.sleep(1)
                    clientLobby()

            else:
                print("_"*91," "*7,"TRANSFERÊNCIA CANCELADA. ENCAMINHANDO PARA O MENU PRINCIPAL..."," "*7,"-"*91)
                time.sleep(2)
                clientLobby()

        elif choice == 3:
            print(" "*7,"CADASTRO\n\n")
            print(" "*7,"NOME:  ",name)
            print(" " * 7,"CPF:   ",cpf)
            print(" " * 7, "Login: ", log_cli)
            print(" " * 7, "Senha:  **********\n")

            alter = input("        DESEJA ALTERAR LOGIN E SENHA ( 1 - SIM / 2 - NÃO)? ")
            alterI = int(alter)

            if alterI == 1:

                print(" "*7,"Área em desenvolvimento. Volte outra hora.\n")
                #new_log = input("        Novo login: ")
                #new_pass = input("        Nova senha: ")

                #cursor.execute(f"UPDATE clientes SET login = '{new_log}' WHERE conta = '{log_cli}'")
                #conexao.commit()
                #cursor.execute(f"SELECT login FROM clientes WHERE login = '{new_log}'")
                #new_logg = cursor.fetchall()
                #login = new_logg

                #cursor.execute(f"UPDATE clientes SET senha = '{new_pass}' WHERE conta = '{account}'")
                #conexao.commit()

                #time.sleep(1)
                #print("\n"," "*6,"_"*36,)
                #print(" "*7,"|   Acesso alterado com sucesso!   |")
                #print(" "*7,"-"*36)
                time.sleep(2)
                clientLobby()

            elif alterI == 2:
                print(" " * 7, "AÇÃO CANCELADA.\n\n")
                clientLobby()
            else:
                print(" " * 7, "INVÁLIDO.\n\n")
                clientLobby()

        elif choice == 4:
            time.sleep(1)
            print(" "*7,"_"*50," "*7)
            print(" "*7,"|   Agradecemos pela sua visita. Volte sempre!   |")
            print(" "*7,"-"*50,"\n")
            time.sleep(2)
            wellcome()

        else:
            print("_"*30," "*7,"|   Opção inválida   |")
            clientLobby()

    except:
        print("\n\n", " " * 6,"Opção inválida, tente novamente.", "\n", " " * 6, "#" * 42, "\n\n")
        time.sleep(2)
        clientLobby()

    else:
        print(" "*7,"_"*50)
        print(" "*7,"|   Obrigado pela preferência. Volte sempre!  |")
        print(" "*7,"-"*50)

wellcome()