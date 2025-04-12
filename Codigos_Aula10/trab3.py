from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    def __init__ (self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property 
    def nome (self):
        return self.__nome
    
    @nome.setter
    def nome (self, valor):
        self.__nome = valor

    @property
    def telefone (self):
        return self.__telefone
    
    @telefone.setter
    def telefone (self, valor):
        self.__telefone = valor
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista (EmpDomestica):

    def __init__ (self, nome, telefone, HorasTrabalhadas, ValorPorHora):
        super().__init__ (nome, telefone)
        self.__HorasTrabalhadas = HorasTrabalhadas
        self.__ValorPorHora = ValorPorHora

    @property
    def HorasTrabalhadas (self):
        return self.__HorasTrabalhadas

    @property 
    def ValorPorHora (self):
        return self.__ValorPorHora

    def getSalario (self):
        return self.__HorasTrabalhadas * self.__ValorPorHora

class Diarista (EmpDomestica):

    def __init__ (self, nome, telefone, DiasTrabalhados, ValorPorDia):
        super().__init__ (nome, telefone)
        self.__DiasTrabalhados = DiasTrabalhados
        self.__ValorPorDia = ValorPorDia

    @property
    def DiasTrabalhados (self):
        return self.__DiasTrabalhados

    @property 
    def ValorPorDia (self):
        return self.__ValorPorDia

    def getSalario (self):
        return self.__DiasTrabalhados * self.__ValorPorDia
    
class Mensalista (EmpDomestica):
    def __init__ (self, nome, telefone, ValorMensal):
        super().__init__ (nome, telefone)
        self.__ValorMensal = ValorMensal

    @property
    def ValorMensal (self):
            return self.__ValorMensal
        
    def getSalario (self):
            return self.__ValorMensal
        
if __name__ == "__main__":

    emp1 = Horista('Ana', '35911111111', 160, 12)
    emp2 = Diarista ('Nazaré', '35922222222', 20, 65)
    emp3 = Mensalista ('Benedita', '35933333333', 1200)
    empregadas = [emp1, emp2, emp3]

    MelhorOpcao = emp1
    print ("Valores Mensais das empregadas:")
    for empregada in empregadas:
        print (f"Nome: {empregada.nome}, Telefone: {empregada.telefone}, Salario: R${empregada.getSalario()}")

        if empregada.getSalario() < MelhorOpcao.getSalario():
            MelhorOpcao = empregada

    print (f"\nA opção mais barata é Nome: {MelhorOpcao.nome}, Telefone: {MelhorOpcao.telefone}, Salário: R${MelhorOpcao.getSalario()}\n")
