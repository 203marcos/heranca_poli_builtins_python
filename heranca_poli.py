from abc import ABCMeta, abstractmethod

class Conta(metaclass = ABCMeta):  #Conta virou uma classe abstrata 

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):  
        pass
    def __str__(self):
        return "[>>codigo {} saldo {}<<]".format(self._codigo, self._saldo)
    
    
class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self._saldo -=2

class ContaPoupanca(Conta):    
    
     def passa_o_mes(self):
        self._saldo *=1.01
        self._saldo -=3
        
class ContaInvestimento(Conta):
    pass
        
        
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes() #duck type, nada como pato, mas não é um pato então faz algo de pato....
  print(conta)
  
class ContaSalario: 

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class MultiploSalario(ContaSalario):
    pass 
    
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1 == conta2)



