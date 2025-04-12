from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria
    
    @cargaHoraria.setter
    def cargaHoraria(self, valor):
        self.__cargaHoraria = valor

    def calculaValorImposto (self, salBruto):
        if salBruto < 1903.9:
            imposto = 0;
        elif salBruto < 2826.66:
            imposto = 15
        elif salBruto < 4664.60:
            imposto = 22.5
        else:
            imposto - 27.5
        return (salBruto * imposto) / 100
    
    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    @property
    def salarioBruto(self):
        return self.__salarioBruto

    @salarioBruto.setter
    def salarioBruto(self, valor):
        self.__salarioBruto = valor

    def calculaSalario(self):
        return self.__salarioBruto

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter
    def salarioHora(self, valor):
        self.__salarioHora = valor

    def calculaSalario(self):
        return self.__salarioHora * self.cargaHoraria

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    prof1.salario = 6000
    prof2.salarioHora = 85
    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.nome, prof.calculaSalario()))

