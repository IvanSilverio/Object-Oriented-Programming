from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade 
        self.__listaDisc = listaDisc       

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade

    ##### Exercício 2 #####
    @property
    def listaDisc(self):
        return self.__listaDisc

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Titulação: {}'.format(self.titulacao))  
        print('Disciplinas ministradas:')
        ##### Exercício 2 #####
        for disc in self.listaDisc:
            print('Nome: {} - Carga Horária: {}'.format(disc.nomeDisc, disc.cargaHoraria))     

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Curso: {}'.format(self.curso)) 
        ##### Exercício 2 #####
        print('Disciplinas cursadas:')
        for disc in self.listaDisc:
            print('Nome: {} - Carga Horária: {}'.format(disc.nomeDisc, disc.cargaHoraria))         

##### Exercício 2 #####
class Disciplina():
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria

    @property
    def nomeDisc(self):
        return self.__nomeDisc

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

if __name__ == "__main__":
    ##### Exercício 2 #####
    disc1 = Disciplina('Programação OO', 64)
    disc2 = Disciplina('Estruturas de dados', 64)
    disc3 = Disciplina('Banco de dados', 64)
    listaDisc1 = [disc1, disc2]
    listaDisc2 = [disc2, disc3]

    prof = Professor('Joao','Av. BPS, 1303', 44, 'doutorado', listaDisc1)
    prof.printDescricao()
    print()
    aluno = Aluno('Pedro','Av. Cesario Alvim, 205', 20, 'SIN', listaDisc2)
    aluno.printDescricao()