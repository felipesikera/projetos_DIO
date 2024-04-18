
def menu():

    menu_escrito = """
    |     #### MENU ####     |
    |                        |
    |     [d] Depositar      |
    |     [s] Sacar          |
    |     [e] Extrato        |
    |     [nu] Novo usuário  |   
    |     [nc] Nova conta    | 
    |     [q] Sair           |
    => """

    return input(menu_escrito)

def criar_usuario(lista_usuarios):
    cpf = input('Digite seu CPF (somente números): ')
    
    # Verifica se o CPF já está cadastrado
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado")
            return None
    
    # Se o CPF não está cadastrado, continua o cadastro
    nome = input('Digite nome e sobrenome: ')
    data_nascimento = input('Digite sua data de nascimento "(XX-XX-XXXX)": ')
    endereco = input('Digite seu endereço (Logradouro, número, bairro e cidade/estado): ')
    
    novo_usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    lista_usuarios.append(novo_usuario)
    print(f'Usuário {novo_usuario["nome"]} cadastrado com sucesso!')
    
    return novo_usuario, lista_usuarios

def criar_conta(lista_usuarios, AGENCIA, lista_contas):
    cpf = input('Digite seu CPF (somente números): ')
    
    # Verifica se o usuário está cadastrado
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            nova_conta = {"agencia": AGENCIA, "conta": len(lista_contas) + 1, "cpf": cpf, "usuario": usuario["nome"]}
            lista_contas.append(nova_conta)
            print("Conta cadastrada")
            print(f'\n### Dados ### \nNome: {nova_conta["usuario"]}\nCPF: {nova_conta["cpf"]}\nAgência: {nova_conta["agencia"]}\nConta: {nova_conta["conta"]}')
            return nova_conta, lista_contas
    
    # Se o loop terminar sem retornar, significa que o usuário não foi encontrado
    print("Usuário não cadastrado. Cadastre um usuário primeiro.")

def deposito(saldo, extrato, valor_deposito, /):

    print("DEPÓSITO")
         
    valor_deposito = float(input("Digite o valor a ser depositado: "))
            
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f'Saldo: R$ {saldo:.2f}')
    else: 
        print("Valor inválido. Repita a operação.")

    return(saldo, extrato)

def saque(*,saldo, extrato, limite, numero_saques, limite_saques):

    # Checa se o usuário possui saques disponíveis

    if numero_saques < limite_saques:
        
        print("SAQUE")
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        # Caso usuário tenha saques disponíveis, checa se possui saldo suficiente para saque

        if (valor_saque > saldo):
            print("Saldo insuficiente. Repita a operação.")
                  
        elif valor_saque <= limite:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f'Saldo: R$ {saldo:.2f}')
            print(f'Saques restantes: {limite_saques - numero_saques}')
        
        # Caso usuário tenha tentado sacar acima do limite permitido

        else: 
            print(f"Limite máximo de saque de R$ {limite:.2f}. Tente novamente.")

    else: 
        print(f'Você atingiu o limite máximo de {limite_saques} saques.')

    return(saldo, extrato, numero_saques)

def exibir_extrato(saldo, /, *, extrato):
    print(f" Extrato ".center(21, "#"))        
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f'Seu salto atual é de R$ {saldo:.2f}')

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_usuarios = []
    lista_contas = []
    valor_deposito = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()
        
        if opcao == "d":
            saldo, extrato = deposito(saldo, extrato, valor_deposito)

        elif opcao == "s":    
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(lista_usuarios)

        elif opcao == "nc":
            criar_conta(lista_usuarios, AGENCIA, lista_contas)

        elif opcao == "q":
            break

        else: 
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

main()
