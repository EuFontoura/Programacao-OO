# Crie um sistema bancário simples usando POO

# A Conta Corrente deve ter um método de sacar cheque especial

# A Conta Poupança deve render juros 

class ContaBancaria: 
    def __init__(self, titular, saldo_inicial=0) -> None:
        self.__titular = titular
        self.__saldo = saldo_inicial

    def  get_titular(self):
        return self.__titular
    
    def  get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def exibir_saldo(self):
        return f"Saldo da conta: {self.__saldo}"

    def depositar(self, valor):
        self.__saldo += valor
        return f"Novo saldo: {self.__saldo}"

    
    def sacar (self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return f"Novo saldo: {self.__saldo}"
        else: 
            return f"Saldo insuficiente. Saldo atual: {self.__saldo}"

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo_inicial=0) -> None:
        super().__init__(titular, saldo_inicial)
        self.__cheque_especial = 500

    def sacar(self, valor):
        saldo_disponivel = self.get_saldo() + self.__cheque_especial
        if valor <= self.get_saldo():
            return super().sacar(valor)
        elif valor <= saldo_disponivel:
            cheque_usado = valor - self.get_saldo()
            self.__cheque_especial -= cheque_usado
            self.__saldo = 0
            return f"Saque usando cheque especial! Novo saldo: 0, Cheque especial disponível: {self.__cheque_especial}"
        else:
            return f"Saldo insuficiente. Saldo e cheque especial somados: {saldo_disponivel}"
        
    def exibir_cheque_especial(self):
        return f"Limite de cheque especial: {self.__cheque_especial}"
            

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial=0) -> None:
        super().__init__(titular, saldo_inicial)
        self.juros = 0.02

    def render_juros(self):
        juros_rendido =  self.get_saldo() * self.juros
        novo_saldo = self.get_saldo() + juros_rendido
        self.set_saldo(novo_saldo)
        return f"A conta poupança rendeu {juros_rendido}, novo saldo: {self.get_saldo()}"


###### Conta Poupança ######
# Exemplo de uso
conta = ContaPoupanca("Alastor", 100)
print(conta.exibir_saldo())
print(conta.render_juros())


###### Conta Corrente ######
# Exemplo de uso
conta = ContaCorrente("João", 100)
print(conta.exibir_saldo())

# Depósito
print(conta.depositar(50))

# Saque normal
print(conta.sacar(120))

# Saque usando cheque especial
print(conta.sacar(450))

# Verificar cheque especial restante
print(conta.exibir_cheque_especial())