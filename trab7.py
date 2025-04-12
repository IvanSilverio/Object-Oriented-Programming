from abc import ABC, abstractmethod
from datetime import date

# Classe que representa os itens de venda
class ItemVenda:
    def __init__(self, codProd, quant, precoUnit):
        self.__codProd = codProd
        self.__quant = quant
        self.__precoUnit = precoUnit

    @property
    def quant(self):
        return self.__quant

    @property
    def precoUnit(self):
        return self.__precoUnit

# Classe abstrata Venda
class Venda(ABC):
    def __init__(self, nroNF, dtEmissao):
        self.__nroNF = nroNF
        self.__dtEmissao = dtEmissao
        self.__itens = []  # Lista de itens de venda

    @property
    def nroNF(self):
        return self.__nroNF

    @property
    def dtEmissao(self):
        return self.__dtEmissao

    # Método para adicionar itens à venda
    def adicionaItem(self, codProd, quant, precoUnit):
        item = ItemVenda(codProd, quant, precoUnit)
        self.__itens.append(item)

    # Método para calcular o total vendido
    def calculaTotalVendido(self):
        total = 0  # Inicialização do total
        for item in self.__itens:
            total += item.quant * item.precoUnit
        return total

    @abstractmethod
    def calculaImposto(self):
        pass

# Classe VendaPF para pessoa física
class VendaPF(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    # Cálculo de imposto para pessoa física (9%)
    def calculaImposto(self):
        total_imposto = 0
        for item in self._Venda__itens:
            total_imposto += 0.09 * item.quant * item.precoUnit
        return total_imposto

# Classe VendaPJ para pessoa jurídica
class VendaPJ(Venda):
    def __init__(self, nroNF, dtEmissao, cnpj, nomeFantasia):
        super().__init__(nroNF, dtEmissao)
        self.__cnpj = cnpj
        self.__nomeFantasia = nomeFantasia

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nomeFantasia(self):
        return self.__nomeFantasia

    # Cálculo de imposto para pessoa jurídica (6%)
    def calculaImposto(self):
        total_imposto = 0
        for item in self._Venda__itens:
            total_imposto += 0.06 * item.quant * item.precoUnit
        return total_imposto

# Código principal
if __name__ == "__main__":
    totalFaturado = 0
    totalImposto = 0
    vendas = []

    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao')
    vendapf.adicionaItem(100, 10, 10)
    vendapf.adicionaItem(100, 10, 20)
    vendapf.adicionaItem(100, 10, 30)
    vendas.append(vendapf)

    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda')
    vendapj.adicionaItem(200, 100, 10)
    vendapj.adicionaItem(201, 100, 20)
    vendas.append(vendapj)

    for venda in vendas:
        totalFaturado += venda.calculaTotalVendido()
        totalImposto += venda.calculaImposto()

    print('Total faturado: {}'.format(totalFaturado))
    print('Total pago em impostos: {}'.format(totalImposto))
