from abc import ABC, abstractmethod

class Transacao():
    def __init__(self, valor, desc):
        self.__valor = valor
        self.__desc = desc

    @property
    def valor(self):
        return self.__valor

    @property
    def desc(self):
        return self.__desc

class Conta(ABC):
    def __init__(self, nroConta, nome, saldo):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__saldo = saldo
        self.__listaTrans = []

    @property
    def nroConta(self):
        return self.__nroConta

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def listaTrans(self):
        return self.__listaTrans        

    def deposito(self, valor, desc):
        self.__listaTrans.append(Transacao(valor, desc))
        self.__saldo += valor

    def saque(self, valor, desc):
        if valor > 0:
            return False
        if self.__saldo + valor < 0:
            return False
        self.__saldo += valor
        self.__listaTrans.append(Transacao(valor, desc))
        return True
    

    def impTransacoes(self):
        print('Transações: ')
        for trans in self.__listaTrans:
            print('Valor: {} - Desc: {}'.format(trans.valor, trans.desc))

    @abstractmethod
    def impExtrato():
        pass

class ContaCorrente(Conta):
    def __init__(self, nroConta, nome, saldo, mensalidade):
        super().__init__(nroConta, nome, saldo)
        self.__mensalidade = mensalidade

    @property
    def mensalidade(self):
        return self.__mensalidade

    def impExtrato(self):
        print('Nro Conta: {}'.format(self.nroConta))
        print('Nome: {}'.format(self.nome))
        print('Saldo: {}'.format(self.saldo))
        print('Mensalidade: {}'.format(self.__mensalidade))
        self.impTransacoes()


class ContaLimite(Conta):
    def __init__(self, nroConta, nome, saldo, limite):
        super().__init__(nroConta, nome, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def saque(self, valor, desc):
        if valor > 0:
            return False
        if self.saldo + self.__limite + valor < 0:
            return False
        self.saldo += valor
        self.listaTrans.append(Transacao(valor, desc))
        return True    

    def impExtrato(self):
        print('Nro Conta: {}'.format(self.nroConta))
        print('Nome: {}'.format(self.nome))
        print('Saldo: {}'.format(self.saldo))        
        print('Saldo + Limite: {}'.format(self.saldo + self.__limite))
        self.impTransacoes()
        
class ContaPoupanca(Conta):
    def __init__(self, nroConta, nome, saldo, diaAniv):
        super().__init__(nroConta, nome, saldo)
        self.__diaAniv = diaAniv
    
    @property
    def diaAniv(self):
        return self.__diaAniv

    def impExtrato(self):
        print('Nro Conta: {}'.format(self.nroConta))
        print('Nome: {}'.format(self.nome))
        print('Saldo: {}'.format(self.saldo))
        print('Dia aniversário: {}'.format(self.__diaAniv))
        self.impTransacoes()

if __name__=="__main__":
    contas = []
    cc = ContaCorrente(1111, 'João Silva', 0, 30)
    cc.deposito(1000, 'Crédito salário')
    if cc.saque(-500, 'Pagto energia'):
        print('Saque de R$500,00 na conta {}'.format(cc.nroConta))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cc.nroConta))
    if cc.saque(-700, 'PIX'):
        print('Saque de R$700,00 na conta {}'.format(cc.nroConta))
    else:
        print('Falha ao realizar saque de R$700,00 na conta {}'.format(cc.nroConta))
    contas.append(cc)

    print()

    cl = ContaLimite(2222, 'Ana Souza', 0, 1000)
    cl.deposito(1500, 'Crédito salário')
    if cl.saque(-1200, 'Pagto boleto'):
        print('Saque de R$1200,00 na conta {}'.format(cl.nroConta))
    else:
        print('Falha ao realizar saque de R$1200,00 na conta {}'.format(cl.nroConta))
    if cl.saque(-500, 'PIX'):
        print('Saque de R$500,00 na conta {}'.format(cl.nroConta))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cl.nroConta))
    contas.append(cl)

    print()

    cp = ContaPoupanca(3333, 'João Silva', 0, 10)
    cp.deposito(1200, 'Econominas')
    if cp.saque(-400, 'Resgate 1'):
        print('Saque de R$400,00 na conta {}'.format(cp.nroConta))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cp.nroConta))
    if cp.saque(-300, 'Resgate 2'):
        print('Saque de R$300,00 na conta {}'.format(cp.nroConta))
    else:
        print('Falha ao realizar saque de R$700,00 na conta {}'.format(cp.nroConta))
    contas.append(cp)

    print()

    for conta in contas:
        conta.impExtrato()
        print()