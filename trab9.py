class NaoEhDoutor(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CpfDuplicado(Exception):
    pass


class Pessoa:
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf
    
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print (f"Nome: {self.nome}, Endereço: {self.endereco}, Idade: {self.idade}, Cpf: {self.cpf}, Titulação: {self.titulacao}")
        print ()

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        print (f"Nome: {self.nome}, Endereço: {self.endereco}, Idade: {self.idade}, Cpf: {self.cpf}, Curso: {self.curso}")
        print ()
    
if __name__ == "__main__":
   
    listaExemplo = [ Professor("Carlos Silva", "Rua das Flores, 123", 40, "123.456.789-00", "Doutor"),
    Aluno("Ana Paula", "Avenida Brasil, 456", 20, "987.654.321-00", "CCO"),
    Professor("João Pereira", "Rua da Esperança, 789", 25, "111.222.333-44", "Mestre"),  # Erro: Idade
    Aluno("Lucas Santos", "Rua Nova, 101", 17, "555.666.777-88", "SIN"),  # Erro: Idade
    Aluno("Mariana Costa", "Rua Verde, 202", 19, "777.888.999-99", "ENG"),  # Erro: Curso
    Aluno("Pedro Lima", "Avenida do Sol, 303", 21, "987.654.321-00", "CCO"),  # Erro: CPF duplicado
    Aluno("Beatriz Oliveira", "Rua das Palmeiras, 404", 19, "333.444.555-66", "SIN")
    ]

    cadastro = []

    for pessoa in listaExemplo:
        if isinstance(pessoa, Professor):
                try:
                    if pessoa.titulacao != 'Doutor':
                        raise NaoEhDoutor()
                    if pessoa.idade < 30:
                        raise IdadeMenorQuePermitida()
                    if pessoa.cpf in [p.cpf for p in cadastro]:
                        raise CpfDuplicado()

                except NaoEhDoutor:
                    print (f"Titulação {pessoa.titulacao} de {pessoa.nome} é inválida.")
                except IdadeMenorQuePermitida:
                    print (f"Idade de {pessoa.nome} menor que permitida: %d" % pessoa.idade)
                except CpfDuplicado:
                    print (f"O cpf {pessoa.cpf} de {pessoa.nome} já foi utilizado.")
                else:
                    cadastro.append(pessoa)

        elif isinstance(pessoa, Aluno):
                try:
                    if pessoa.curso not in ('CCO', 'SIN'):
                        raise CursoInvalido()
                    if pessoa.idade < 18:
                        raise IdadeMenorQuePermitida()
                    if pessoa.cpf in [p.cpf for p in cadastro]:
                        raise CpfDuplicado()

                except CursoInvalido:
                    print (f"O curso {pessoa.curso} de {pessoa.nome} é inválido.")
                except IdadeMenorQuePermitida:
                    print (f"Idade de {pessoa.nome} menor que permitida: %d" % pessoa.idade)
                except CpfDuplicado:
                    print (f"O cpf {pessoa.cpf} de {pessoa.nome} já foi utilizado.")
                else:
                    cadastro.append(pessoa)
                
    for pessoa in cadastro:
        pessoa.printDescricao() 
                