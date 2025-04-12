from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    @property 
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
class Professor(Pessoa):
    def __init__(self, nome, email, titulacao):
        super().__init__(nome, email)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
class Aluno(Pessoa):
    def __init__(self, nome, email, nroMatric, curso):
        super().__init__(nome, email)
        self.__nroMatric = nroMatric
        self.__curso = curso

    @property
    def nroMatric(self):
        return self.__nroMatric
    
    @property
    def curso(self):
        return self.__curso
    
class Disciplina():
    def __init__(self, nome, cargaHoraria):
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self.__nome    

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria


class Curso():
    def __init__(self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome
        self.__grade = []

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome    

    @property
    def grade(self):
        return self.__grade
    
    def addDisciplina(self, discip):
        self.__grade.append(discip)


class Turma():
    def __init__(self, nome, disciplina, professor):
        self.__nome = nome
        self.__disciplina = disciplina
        self.__professor = professor
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def disciplina(self):
        return self.__disciplina

    @property
    def professor(self):
        return self.__professor
    
    @property
    def alunos(self):
        return self.__alunos
    
    def addAluno(self, aluno):
        self.__alunos.append(aluno)
        
if __name__ == "__main__":
    ### Criando disciplinas ###
    disc1 = Disciplina('Cálculo 1', 64)
    disc2 = Disciplina('Programação OO', 64)
    disc3 = Disciplina('Estruturas de dados', 64)
    disc4 = Disciplina('Banco de dados', 64)
    disc5 = Disciplina('Sistemas Embarcados', 64)
    disc6 = Disciplina('Economia', 48)
    disc7 = Disciplina('Gestão do Conhecimento', 48)
    disc8 = Disciplina('Empreendedorismo Tecnológico', 48)

    ### Criando cursos###
    curso1 = Curso('CCO', 'Ciência da Computação')
    curso1.addDisciplina(disc1)
    curso1.addDisciplina(disc2)
    curso1.addDisciplina(disc3)
    curso1.addDisciplina(disc4)
    curso1.addDisciplina(disc5)
    curso1.addDisciplina(disc6)
    curso2 = Curso('SIN', 'Sistemas de Informação')
    curso2.addDisciplina(disc2)
    curso2.addDisciplina(disc3)
    curso2.addDisciplina(disc4)
    curso2.addDisciplina(disc6)
    curso2.addDisciplina(disc7)
    curso2.addDisciplina(disc8)

    ### Criando professores ###
    prof1 = Professor('Antônio', 'antonio@unifei.edu.br', 'doutor')
    prof2 = Professor('Laercio', 'laercio@unifei.edu.br', 'doutor')
    prof3 = Professor('Melise', 'melise@unifei.edu.br', 'doutor')
    prof4 = Professor('Bruno', 'bruno@unifei.edu.br', 'doutor')
    prof5 = Professor('Adriana', 'adriana@unifei.edu.br', 'doutor')
    prof6 = Professor('Isabela', 'isabela@unifei.edu.br', 'doutor')

    ### Criando alunos ###
    aluno1 = Aluno('Aluno1', 'aluno1@unifei.edu.br', '54321', curso1)
    aluno2 = Aluno('Aluno2', 'aluno2@unifei.edu.br', '54322', curso1)
    aluno3 = Aluno('Aluno3', 'aluno3@unifei.edu.br', '54323', curso1)    
    aluno4 = Aluno('Aluno4', 'aluno4@unifei.edu.br', '54324', curso1)
    aluno5 = Aluno('Aluno5', 'aluno5@unifei.edu.br', '54325', curso1)
    aluno6 = Aluno('Aluno6', 'aluno6@unifei.edu.br', '54326', curso2)
    aluno7 = Aluno('Aluno7', 'aluno7@unifei.edu.br', '54327', curso2)
    aluno8 = Aluno('Aluno8', 'aluno8@unifei.edu.br', '54328', curso2)
    aluno9 = Aluno('Aluno9', 'aluno9@unifei.edu.br', '54329', curso2)

    ### Criando turmas ###
    listaTurmas = []
    turma1 = Turma('T1', disc1, prof1)
    turma1.addAluno(aluno1)
    turma1.addAluno(aluno2)
    turma1.addAluno(aluno3)
    turma1.addAluno(aluno4)
    turma1.addAluno(aluno5)
    turma1.addAluno(aluno6)
    listaTurmas.append(turma1)
    turma2 = Turma('T2', disc2, prof2)
    turma2.addAluno(aluno1)
    turma2.addAluno(aluno2)
    turma2.addAluno(aluno3)
    turma2.addAluno(aluno4)
    turma2.addAluno(aluno5)
    turma2.addAluno(aluno6)
    turma2.addAluno(aluno7)
    turma2.addAluno(aluno8)
    turma2.addAluno(aluno9)
    listaTurmas.append(turma2)
    turma3 = Turma('T3', disc3, prof3)
    turma3.addAluno(aluno1)
    turma3.addAluno(aluno2)
    turma3.addAluno(aluno3)
    turma3.addAluno(aluno4)
    turma3.addAluno(aluno5)
    turma3.addAluno(aluno6)
    turma3.addAluno(aluno7)
    turma3.addAluno(aluno8)
    turma3.addAluno(aluno9)
    listaTurmas.append(turma3)
    turma4 = Turma('T4', disc4, prof3)    
    turma4.addAluno(aluno1)
    turma4.addAluno(aluno2)
    turma4.addAluno(aluno3)
    turma4.addAluno(aluno4)
    turma4.addAluno(aluno5)
    turma4.addAluno(aluno6)
    turma4.addAluno(aluno7)
    turma4.addAluno(aluno8)
    turma4.addAluno(aluno9)
    listaTurmas.append(turma4)    
    turma5 = Turma('T5', disc5, prof4)
    turma5.addAluno(aluno1)
    turma5.addAluno(aluno2)
    turma5.addAluno(aluno3)
    turma5.addAluno(aluno4)
    turma5.addAluno(aluno5)
    turma5.addAluno(aluno6)
    listaTurmas.append(turma5)  
    turma6 = Turma('T6', disc6, prof5)
    turma6.addAluno(aluno1)
    turma6.addAluno(aluno2)
    turma6.addAluno(aluno3)
    turma6.addAluno(aluno4)
    turma6.addAluno(aluno5)
    turma6.addAluno(aluno6)
    turma6.addAluno(aluno7)
    turma6.addAluno(aluno8)
    turma6.addAluno(aluno9)
    listaTurmas.append(turma6)
    turma7 = Turma('T7', disc7, prof5)
    turma7.addAluno(aluno6)
    turma7.addAluno(aluno7)
    turma7.addAluno(aluno8)
    turma7.addAluno(aluno9)
    listaTurmas.append(turma7)
    turma8 = Turma('T8', disc8, prof5)
    turma8.addAluno(aluno6)
    turma8.addAluno(aluno7)
    turma8.addAluno(aluno8)
    turma8.addAluno(aluno9)    
    listaTurmas.append(turma8)


    ### Questão 2
    ### Informe a quantidade de alunos matriculados em turmas de disciplinas da grade de CCO (curso1)
    quant = 0
    for turma in listaTurmas:
        if turma.disciplina in curso1.grade:
            quant = quant + len(turma.alunos)
    print('Quantidade de alunos matriculados em turmas de CCO: ' + str(quant))
    print()

    ### Questão 3
    ### Liste as disciplinas ministradas pela Profa. Adriana (prof5)
    listaDisc= []
    for turma in listaTurmas:
        if turma.professor == prof5:
            listaDisc.append(turma.disciplina)
    print('Disciplinas ministradas pela Profa. Adriana: ')
    for disc in listaDisc:
        print(disc.nome)
    print()    

    ### Informe a carga horária do Aluno9
    cargaHor = 0
    for turma in listaTurmas:
        if aluno9 in turma.alunos:
            cargaHor = cargaHor + turma.disciplina.cargaHoraria
    print('Carga horária do Aluno9:' + str(cargaHor))
    print()

    ### Informe a carga horária de todos os professores que possuem turmas
    dic = {}
    for turma in listaTurmas:
        if turma.professor.nome in dic.keys():
            ch = turma.disciplina.cargaHoraria + dic[turma.professor.nome]
        else:
            ch = turma.disciplina.cargaHoraria
        dic[turma.professor.nome] = ch
    print('Carga horária dos professores: ')    
    for chaves, valores in dic.items():
        print('Nome: {} - CH: {}'.format(chaves, valores))