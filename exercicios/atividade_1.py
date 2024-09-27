
class Conta:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.__numero_conta = numero_conta  
        self.__saldo = saldo_inicial  

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta {self.__numero_conta}: R${self.__saldo:.2f}")

    def get_numero_conta(self):
        return self.__numero_conta

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []  

    def adicionar_conta(self, conta_bancaria):
        self.contas.append(conta_bancaria)
        print(f"Conta {conta_bancaria.get_numero_conta()} adicionada ao cliente {self.nome}.")

    def exibir_contas(self):
        print(f"Contas de {self.nome}:")
        for conta in self.contas:
            conta.exibir_saldo()


conta1 = Conta("12345-6", 500)
conta2 = Conta("65432-1", 1000)

cliente = Cliente("João")

cliente.adicionar_conta(conta1)
cliente.adicionar_conta(conta2)

cliente.exibir_contas()

conta1.depositar(200)
conta2.sacar(300)

cliente.exibir_contas()
