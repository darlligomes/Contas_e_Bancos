from abc import ABC, abstractmethod
from ContaBancaria import *

class Pessoa(ABC):
    def __init__(self, nomeCliente, idade):
        self._nomeCliente = nomeCliente  
        self.idade = idade
    
    @property
    def nomeCliente (self):
        return self._nomeCliente
            
    @nomeCliente.setter
    def nomeCliente(self, nomeCliente):
        self._nomeCliente = nomeCliente
        
class Cliente(Pessoa):
    def __init__(self, nomeCliente, idade):
        super().__init__(nomeCliente, idade)
        self._nome = nomeCliente
        self.idade = idade
        self.contas = {}  

    def exibir_cliente_dados(self):
        dados_cliente = self.__dict__.copy()  
        contas_dict = {}
        for tipo_conta, conta in self.contas.items():
            contas_dict[tipo_conta] = conta.__dict__
        dados_cliente['contas'] = contas_dict
        return dados_cliente

    def DeletarConta(self, tipo_conta):
        if tipo_conta in self.contas:
            del self.contas[tipo_conta]
            print(f"Conta {tipo_conta} excluída com sucesso.")
        else:
            print(f"O cliente não possui conta {tipo_conta} para excluir.")

    def AdicionarConta(self, conta): 
        tipo_conta = type(conta).__name__
        if tipo_conta in self.contas:
            confirmacao = input(f"O cliente já possui uma ou mais contas {tipo_conta}. Deseja adicionar outra conta desse tipo? (Sim/Nao): ").strip().upper()
            if confirmacao[:1] == 'N':
                print("Ação cancelada.")
                return
        else:
            self.contas[tipo_conta] = []  
        
        self.contas[tipo_conta].append(conta)
        print(f"{tipo_conta} adicionada ao cliente {self.nomeCliente}.")


    def ExibirContas(self):
        if self.contas:
            return [conta.exibirConta() for conta in self.contas.values()]
        else:
            return "Sem contas associadas"
