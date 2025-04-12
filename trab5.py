from abc import ABC, abstractmethod

# Classe responsável por registrar o ponto do funcionário em um determinado mês e ano
class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    # Propriedades para acessar mês, ano, número de faltas e atrasos
    @property
    def mes(self):
        return self.__mes
        
    @property
    def ano(self):
        return self.__ano
        
    @property
    def nroFaltas(self):
        return self.__nroFaltas
        
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
        
    # Métodos para lançar faltas e atrasos
    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas = nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos = nroAtrasos


# Classe abstrata para os funcionários (Professor e Técnico Administrativo)
class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []  # Lista que guarda os pontos mensais de cada funcionário

    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def nome(self):
        return self.__nome
        
    # Adiciona um ponto (registro de faltas e atrasos) para um determinado mês e ano
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        ponto = PontoFunc(mes, ano, faltas, atrasos)
        self.__pontoMensalFunc.append(ponto)

    # Métodos para lançar faltas e atrasos em um mês e ano específicos
    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaAtrasos(atrasos)
                
    # Imprime a folha de pagamento do funcionário
    def imprimeFolha(self, mes, ano):
        salario = self.calculaSalario(mes, ano)  # Chama o cálculo do salário
        bonus = self.calculaBonus(mes, ano)      # Chama o cálculo do bônus
        print(f"Codigo: {self.__codigo}")
        print(f"Nome: {self.__nome}")
        print(f"Salario Liquido: {salario:.2f}")
        print(f"Bonus: {bonus:.2f}")

    # Métodos abstratos que serão implementados pelas subclasses
    @abstractmethod 
    def calculaSalario(self, mes, ano):
        pass
    
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass


# Classe Professor, herda de Funcionario
class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    # Propriedades para acessar os atributos de Professor
    @property
    def titulacao(self):
        return self.__titulacao
        
    @property
    def salarioHora(self):
        return self.__salarioHora
        
    @property
    def nroAulas(self):
        return self.__nroAulas
        
    # Calcula o salário do professor com base nas horas trabalhadas e faltas
    def calculaSalario(self, mes, ano):
        for ponto in self._Funcionario__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroFaltas = ponto.nroFaltas
                return self.__salarioHora * self.__nroAulas - self.__salarioHora * nroFaltas
        return 0  # Retorna 0 caso o ponto não seja encontrado
        
    # Calcula o bônus do professor com base na pontualidade
    def calculaBonus(self, mes, ano):
        salario = self.calculaSalario(mes, ano)
        for ponto in self._Funcionario__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroAtrasos = ponto.nroAtrasos
                bonus = 0.10 * salario - (nroAtrasos / 100) * salario
                return bonus
        return 0  # Retorna 0 caso o ponto não seja encontrado


# Classe Técnico Administrativo, herda de Funcionario
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    # Propriedades para acessar os atributos de Técnico Administrativo
    @property
    def funcao(self):
        return self.__funcao
        
    @property
    def salarioMensal(self):
        return self.__salarioMensal
               
    # Calcula o salário do técnico administrativo com base nas faltas
    def calculaSalario(self, mes, ano):
        for ponto in self._Funcionario__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroFaltas = ponto.nroFaltas
                return self.__salarioMensal - (self.__salarioMensal / 30) * nroFaltas
        return 0  # Retorna 0 caso o ponto não seja encontrado
               
    # Calcula o bônus do técnico administrativo com base na pontualidade
    def calculaBonus(self, mes, ano):
        salario = self.calculaSalario(mes, ano)
        for ponto in self._Funcionario__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroAtrasos = ponto.nroAtrasos
                bonus = 0.08 * salario - (nroAtrasos / 100) * salario
                return bonus
        return 0  # Retorna 0 caso o ponto não seja encontrado


# Código de teste principal
if __name__ == "__main__":
    funcionarios = []
    
    prof = Professor(1, "Joao", "Doutor", 45.35, 32) 
    prof.adicionaPonto(4, 2021, 2, 3)
    funcionarios.append(prof)
    
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 3, 4)
    funcionarios.append(tec)
    
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()
