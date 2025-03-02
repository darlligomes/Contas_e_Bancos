from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, _numero, _agencia, cliente, saldo=0):
        self.saldo = saldo
        self.agencia = _agencia
        self.numero = _numero
        self.cliente = cliente
    

    @abstractmethod   
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return f'Foi realizado o depósito de R$ {valor:.2f}'

    
    def exibirSaldo(self):
        return f'Saldo: R$ {self.saldo:.2f}'

    
    def exibirConta(self):
        if self.cliente:  
            return f'Agencia: {self.agencia} || Cliente: {self.cliente.nomeCliente} || Numero: {self.numero}'
        else:
            return "Sem cliente associado"
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero): 
        self._numero = numero
        
    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self, agencia): 
        self._agencia = agencia
    
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, saldo, limite_extra):
        super().__init__(numero, agencia, cliente, saldo)   
        self.limite_extra = limite_extra
            
    def sacar(self, valor):
        saldo_disponivel = self.saldo + self.limite_extra
        if valor <= saldo_disponivel:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                valor_restante = valor - self.saldo
                self.saldo = 0
                self.limite_extra -= valor_restante
            return f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}, Limite Extra restante: R$ {self.limite_extra:.2f}"
        else:
            return f"Saque de R$ {valor:.2f} não autorizado. Saldo insuficiente, incluindo o limite extra." 
             
class ContaPoupanca(Conta):
    def __init__(self, numero, agencia, cliente, saldo):
        super().__init__(numero, agencia, cliente, saldo)
        
    def sacar(self, valor):
        if (self.saldo >= valor): 
            self.saldo = self.saldo - valor
            return self.exibirSaldo()
        else:
            return 'Saldo insuficiente'
   
