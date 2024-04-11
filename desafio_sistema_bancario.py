menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        print("DEPÓSITO")
        
        deposito = float(input("Digite o valor a ser depositado: "))
        
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print(f'Saldo: R$ {saldo:.2f}')
        else: 
            print("Valor inválido. Repita a operação.")

    elif opcao == "s":
        print("SAQUE")
        
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))

            if (saque > saldo):
                print("Saldo insuficiente. Repita a operação.")
            
            elif saque <= limite:
                saldo -= saque
                numero_saques += 1
                extrato.append(f"Saque: R$ {saque:.2f}")
                print(f'Saldo: R$ {saldo:.2f}')
                print(f'Limite de saques: {LIMITE_SAQUES-numero_saques}')
            else: 
                print(f"Limite máximo de saque de R$ {limite:.2f}. Tente novamente.")

        else: 
            print(f'Você atingiu o limite máximo de {LIMITE_SAQUES} saques.')
        

    elif opcao == "e":
        print("Extrato")
        
        if extrato is []:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f'Seu salto atual é de R$ {saldo:.2f}')

    elif opcao == "q":
        break

    else: 
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
