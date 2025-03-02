from RelacaoPessoa import Cliente
from ContaBancaria import *
from Banco import *
import pprint as p

def criar_banco(bancos):
    nome_banco = input("Informe o nome do banco: ")
    novo_banco = Banco(nome_banco)
    bancos.append(novo_banco)
    print(f"Banco {novo_banco.nomeBanco} criado com sucesso.")

def criar_cliente():
    nome = input("Informe o nome do cliente: ")
    idade = int(input("Informe a idade do cliente: "))
    if idade < 18: 
        print("O cliente deve ser maior de 18 anos para abrir uma conta.")
        return 
    else:
        return Cliente(nome, idade)

def criar_conta(cliente, banco):
    tipo_conta = input("Informe o tipo de conta (Corrente/Poupança): ").strip().lower()
    numero = int(input("Informe o número da conta: "))
    agencia = int(input("Informe a agência da conta: "))
    saldo_inicial = float(input("Informe o saldo inicial: "))

    if not banco.AutenticarAg(agencia):
        print(f"A agência {agencia} não está cadastrada no banco {banco.nomeBanco}. Por favor, cadastre a agência primeiro.")
        return

    if tipo_conta == "corrente":
        limite_extra = float(input("Informe o limite extra da conta corrente: "))
        nova_conta = ContaCorrente(numero, agencia, cliente.nomeCliente, saldo_inicial, limite_extra)
        nome_tipo = "Corrente"
    elif tipo_conta == "poupança" or tipo_conta == "poupanca":
        nova_conta = ContaPoupanca(numero, agencia, cliente.nomeCliente, saldo_inicial)
        nome_tipo = "Poupança"
    else:
        print("Tipo de conta inválido. Use 'Corrente' ou 'Poupança'.")
        return

    cliente.AdicionarConta(nova_conta)
    banco.inserir_conta(nova_conta)
    banco.inserir_cliente(cliente)
    print(f"Conta {nome_tipo} criada para {cliente.nomeCliente} no banco {banco.nomeBanco}.")

     
def criar_banco():
    nome_banco = input("Informe o nome do banco: ")
    banco = Banco(nome_banco)
    return banco

def exibir_menu():
    print("""
Opções:
1. Criar Cliente
2. Criar Conta para Cliente
3. Criar Banco
4. Exibir Agências do Banco
5. Inserir Agência no Banco
6. Autenticar Conta
7. Sacar Dinheiro de Conta
8. Exibir Clientes Criados
9. Exibir saldo do Cliente
10. Realizar Depósito em Conta
11. Dicionário dos dados
12. Exibir contas de um cliente
13. Sair
""")


def main():
    clientes = []
    bancos = []
    
    print("Movimentações Financeiras e etcs")
    nome_banco = input("Informe o nome do banco: ")
    banco = Banco(nome_banco)
    bancos.append(banco)
    print(f"Banco {banco.nomeBanco} criado com sucesso.")
    
    while True:
        opcao_agencia = input("Deseja inserir uma agência no banco? (Sim/Não): ").strip().lower()
        if opcao_agencia == 'sim':
            agencia = int(input("Informe o número da agência: "))
            banco.inserirAgencia(agencia)
            print(f"Agência {agencia} inserida no banco {banco.nomeBanco}.")
        elif opcao_agencia == 'não' or opcao_agencia == 'nao':
            break
        else:
            print("Opção inválida. Digite 'Sim' ou 'Não'.")
                  
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":       
            novoCliente = criar_cliente()
            clienteExiste = next((cliente for cliente in clientes if cliente.nomeCliente == novoCliente.nomeCliente), None)
            if clienteExiste:
                print("Esse cliente já existe.")
                continue
            else:
                clientes.append(novoCliente)
                print(f"Cliente {novoCliente.nomeCliente} criado com sucesso.")
        
        elif escolha == "2":
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            nome_cliente = input("Informe o nome do cliente para criar conta: ")
            cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
            if cliente:
                criar_conta(cliente, banco) 
            else:
                print("Cliente não encontrado.")

        
        elif escolha == "3":
            banco = criar_banco()
            print(f"Banco {banco.nomeBanco} criado com sucesso.")
        
        elif escolha == "4":
            if banco:
                print(banco.exibirAgencias())
            else:
                print("Nenhum banco criado.")
        
        elif escolha == "5":
            if banco:
                agencia = int(input("Informe a agência para inserir no banco: "))
                banco.inserirAgencia(agencia)
                print(f"Agência {agencia} inserida no banco {banco.nomeBanco}.")
            else:
                print("Nenhum banco criado.")
        
        elif escolha == "6":
            if banco:
                nome_cliente = input("Informe o nome do cliente para autenticar: ")
                cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
                if cliente:
                    resultado = banco.Autenticacao(cliente)
                    print(resultado)
                else:
                    print("Cliente não encontrado.")
            else:
                print("Nenhum banco criado.")

        elif escolha == "7":
            nome_banco = input("Informe o nome do banco: ")
            banco = next((b for b in bancos if b.nomeBanco == nome_banco), None)
            if banco:
                nome_cliente = input("Informe o nome do cliente para sacar: ")
                cliente = next((c for c in clientes if c.nomeCliente == nome_cliente), None)
                if cliente and cliente.contas:
                    tipo_conta_escolhido = input("De qual conta deseja sacar (Corrente/Poupança)? ").strip().lower()
                    if tipo_conta_escolhido == "corrente":
                        tipo_conta = "ContaCorrente"
                    elif tipo_conta_escolhido in ["poupança", "poupanca"]:
                        tipo_conta = "ContaPoupanca"
                    else:
                        print("Tipo de conta inválido.")
                        continue

                    contas_tipo = cliente.contas.get(tipo_conta, [])
                    if contas_tipo:
                        print("Contas disponíveis:")
                        for indice, conta in enumerate(contas_tipo, start=1):
                            print(f"{indice}. Conta Número: {conta.numero}, Agência: {conta.agencia}")
                        try:
                            escolha_conta = int(input("Selecione qual é a conta desejada (Pelo número na ordem): "))
                            if escolha_conta < 1 or escolha_conta > len(contas_tipo):
                                print("Opção inválida.")
                                continue
                            conta = contas_tipo[escolha_conta - 1]
                            valor_saque = float(input("Informe o valor para saque: "))
                            print(conta.sacar(valor_saque))
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número válido.")
                            continue
                    else:
                        print(f"O cliente não possui conta(s) do tipo {tipo_conta_escolhido}.")
                else:
                    print("Cliente não encontrado ou sem contas associadas.")
            else:
                print("Banco não encontrado.")

        elif escolha == "8":
            if clientes:
                print("\nClientes Criados:")
                for cliente in clientes:
                    print(f"- {cliente.nomeCliente}, Idade: {cliente.idade}")
            else:
                print("Nenhum cliente criado.")
                
        elif escolha == '9':
            nome_cliente = input("Informe o nome de um cliente: ")
            cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
            if cliente is None or not cliente.contas:
                print("Cliente não encontrado ou sem contas associadas.")
            else:
                for tipo_conta, lista_contas in cliente.contas.items():
                    for conta in lista_contas:
                        if isinstance(conta, ContaCorrente):
                            saldo_total = conta.saldo + conta.limite_extra
                            print(f"Saldo da {tipo_conta}: R$ {saldo_total:.2f} (Saldo + Limite Extra)")
                        elif isinstance(conta, ContaPoupanca):
                            print(f"Saldo da {tipo_conta}: R$ {conta.saldo:.2f}")
                        else:
                            print(f"Tipo de conta desconhecido: {tipo_conta}")

        elif escolha == '10':
            nome_cliente = input("Informe o nome de um cliente:\n")
            cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
            if cliente is None or not cliente.contas:
                print("Cliente não encontrado ou sem contas associadas.")
            else:
                tipo_conta_escolhido = input("Em qual conta deseja depositar (Corrente/Poupança)? ").strip().lower()
                tipo_conta = "ContaCorrente" if tipo_conta_escolhido == "corrente" else "ContaPoupanca"
                
                contas_tipo = cliente.contas.get(tipo_conta, [])
                
                if contas_tipo:
                    print("Contas disponíveis:")
                    for indice, conta in enumerate(contas_tipo, start=1):
                        print(f"{indice}. Conta Número: {conta.numero}, Agência: {conta.agencia}")
                    
                    try:
                        escolha_conta = int(input("Selecione o número da conta desejada: "))
                        if 1 <= escolha_conta <= len(contas_tipo):
                            conta = contas_tipo[escolha_conta - 1]
                            deposito = float(input("Informe o valor para depositar:\n"))
                            print(conta.depositar(deposito))
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")
                else:
                    print(f"O cliente não possui conta {tipo_conta_escolhido}.")

        elif escolha == '11':
            nome_cliente = input("Informe o nome de um cliente:\n")
            cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
            if cliente:
                p.pprint(cliente.exibir_cliente_dados())
            else:
                print("Cliente não encontrado.")

        elif escolha == '12':
            nome_cliente = input("Informe o nome de um cliente:\n")
            cliente = next((cliente for cliente in clientes if cliente.nomeCliente == nome_cliente), None)
            if cliente:
                print(f"\nContas do cliente {cliente.nomeCliente}:")
                for tipo_conta, contas in cliente.contas.items():
                    print(f"\nTipo de conta: {tipo_conta}")
                    for conta in contas: 
                        print(f"  Número: {conta.numero}")
                        print(f"  Agência: {conta.agencia}")
                        print(f"  Saldo: R$ {conta.saldo:.2f}")
                        if isinstance(conta, ContaCorrente):
                            print(f"  Limite Extra: R$ {conta.limite_extra:.2f}")
            else:
                print("Cliente não encontrado.")
      
                
        elif escolha == "13":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()