from abc import ABC, abstractmethod
from datetime import date

class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self._nroConta = nroConta
        self._nome = nome
        self._limite = limite
        self._senha = senha
        self._transacoes = [] #sua vez, agrega todas as transações realizadas por meio de uma lista chamada transacoes

    # Getters e Setters para Conta
    @property
    def nroConta(self):
        return self._nroConta

    @nroConta.setter
    def nroConta(self, novo_nroConta):
        self._nroConta = novo_nroConta

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def transacoes(self):
        return self._transacoes
    

    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        self._transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        
        if self.senha == senha and self.calculaSaldo() >= valor:
                saque = Saque(valor, data, senha)
                self._transacoes.append(saque)
                return True
        else:
                return False
        
                
                
        

    def adicionaTransf(self, valor, data, senha, contaFavorecida):
        if (self.calculaSaldo() + self._limite) > valor:
            debito = Transferencia(valor, data, senha, 'D')
            credito = Transferencia(valor, data, senha, 'C')
            self.transacoes.append(debito)
            contaFavorecida.transacoes.append(credito)
            return True
        return False


    def calculaSaldo(self):
        total = 0

        for saldos in self.transacoes:
            
            if isinstance(saldos, Deposito):
                total += saldos.valor

            elif isinstance(saldos, Saque):
                total -= saldos.valor

            else:
                if saldos.tipoTransf == 'C':
                    total += saldos.valor
                else:
                    total -= saldos.valor


        return total + self.limite

class Transacao(ABC):
    def __init__(self, valor, data):
        self._valor = valor
        self._data = data

    # Getters e Setters para Transacao
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nova_data):
        self._data = nova_data



class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self._senha = senha

     # Getters e Setters para Saque
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha



class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self._senha = senha
        self._tipoTransf = tipoTransf

    # Getters e Setters para Transferencia
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def conta_destino(self):
        return self._conta_destino

    @conta_destino.setter
    def conta_destino(self, nova_conta_destino):
        self._conta_destino = nova_conta_destino

    @property
    def tipoTransf(self):
        return self._tipoTransf



class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.nomeDepositante = nomeDepositante

    # Getters e Setters para Deposito
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor





if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha errada') == False:
        print('Não foi possível realizar o saque no valor de 1000')
    
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria d a Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    
    print('------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700

""" MODO GPT
   
   from abc import ABC
from datetime import date

class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []  # Lista para armazenar as transações

    @property
    def nroConta(self):
        return self.__nroConta

    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    @property
    def senha(self):
        return self.__senha

    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        self.__transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha or self.calculaSaldo() < valor:
            return False
        saque = Saque(valor, data, senha)
        self.__transacoes.append(saque)
        return True

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        # Verifica se o saldo disponível (saldo + limite) é suficiente para a transferência
        if senha != self.__senha or self.calculaSaldo() < valor:
            return False

        # Débito na conta corrente
        transf_debito = Transferencia(valor, data, senha, 'D')
        self.__transacoes.append(transf_debito)

        # Crédito na conta favorecida
        transf_credito = Transferencia(valor, data, senha, 'C')
        contaFavorecido.__transacoes.append(transf_credito)

        return True

    def calculaSaldo(self):
        saldo = self.__limite  # Inicializa o saldo com o limite
        
        for transacao in self.__transacoes:
            # Verifica se a transação é um depósito
            if isinstance(transacao, Deposito):
                saldo += transacao.valor  # Depósito aumenta o saldo
            # Verifica se a transação é um saque ou transferência de débito
            elif isinstance(transacao, (Saque, Transferencia)) and transacao.tipoTransf == 'D':
                saldo -= transacao.valor  # Saque ou transferência de débito diminui o saldo
        return saldo


class Transacao(ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data


class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha
        self.tipoTransf = 'D'  # Saque é um débito


class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante
        self.tipoTransf = 'C'  # Depósito é um crédito


class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.tipoTransf = tipoTransf  # Define se é débito (D) ou crédito (C)


if __name__ == "__main__":

    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')

    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')

    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:  # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')

    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')

    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')

    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # deve imprimir 1700 """
