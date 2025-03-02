from RelacaoPessoa import *

class Banco:
    def __init__(self, nomeBanco):
        self.nomeBanco = nomeBanco
        self.agencias = []
        self.numeros = [] 
        self.clientes = []
      
    def exibirAgencias(self):
        if self.agencias:
            return "Agências cadastradas: \n" + '\n'.join(str(agencia) for agencia in self.agencias)
        else: 
            return "Sem agências cadastradas."

    def inserirAgencia(self, agencia):
        if agencia not in self.agencias:
            self.agencias.append(agencia)
            print(f"Agência {agencia} adicionada com sucesso.")
        else:
            print(f"A agência {agencia} já está cadastrada.")

    def inserir_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def inserir_conta(self, conta):
        if conta.numero not in self.numeros:
            self.numeros.append(conta.numero)
        else:
            print(f"O número de conta {conta.numero} já existe neste banco.")

    def Autenticacao(self, cliente):
        if not cliente.contas:
            return f"Cliente {cliente.nomeCliente} não possui contas no banco {self.nomeBanco}."

        contas_autenticadas = []
        for lista_contas in cliente.contas.values():
            for conta in lista_contas:
                if (self.AutenticarAg(conta.agencia) and
                    self.AutenticarNumero(conta.numero) and
                    self.AutenticarCliente(cliente)):
                    contas_autenticadas.append(conta)

        if contas_autenticadas:
            numeros_contas = ', '.join(str(conta.numero) for conta in contas_autenticadas)
            return f"Cliente {cliente.nomeCliente} autenticado nas contas: {numeros_contas}."
        else:
            return f"O cliente {cliente.nomeCliente} não possui contas autenticadas neste banco."

                                   
    def AutenticarAg(self, agencia):
        return agencia in self.agencias

    def AutenticarNumero(self, numero):
        return numero in self.numeros

    def AutenticarCliente(self, cliente):
        return cliente in self.clientes
