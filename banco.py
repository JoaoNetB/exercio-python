
programa = True
saldo = 0


def funcaoDepositar(valor):
    if valor > 0 and valor < 2147483647:
        global saldo
        
        saldo += valor
    else:
        print("Adicione um valor válido")



def funcaoSacar(valor):
    
    global saldo

    if saldo - valor >= 0:
        saldo -= valor
    else:
        print("Saldo insuficiente para o saque")



    


# Programa principal
while programa:
    print("Saldo: R${}" .format(saldo))

    print("O que você quer fazer ?")
    print("1. Depositar\n2. Sacar\n3. Sair")

    opcao = str(input("Sua opcao: "))

    if opcao == "1":

        try:
            resultado = int(input("Qual valor? "))
        
            funcaoDepositar(resultado)
        except:
            print("Digite um valor numérico")

    elif opcao == "2":
        
        try:
            resultado = int(input("Qual valor? "))

            funcaoSacar(resultado)
        except:
            print("Digite um valor numérico")

    elif opcao == "3":

        programa = False
    
    else:
        print("Digite uma das três opções")
        



    