import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

class Aluno:
    def __init__(self, cpf, nome, email, tipo_aula, professor, numero_aulas):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__tipo_aula = tipo_aula
        self.__professor = professor
        self.__numero_aulas = numero_aulas

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @property
    def tipo_aula(self):
        return self.__tipo_aula
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def numero_aulas(self):
        return self.__numero_aulas


class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaProfessores):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Cadastro de Aluno")
        self.controle = controle

        # Frames
        self.framecpfAluno = tk.Frame(self)
        self.framenomeAluno = tk.Frame(self)
        self.frameemailAluno = tk.Frame(self)
        self.frameTipoAula = tk.Frame(self)
        self.frameProfessor = tk.Frame(self)
        self.frameNumeroAulas = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framecpfAluno.pack()
        self.framenomeAluno.pack()
        self.frameemailAluno.pack()
        self.frameTipoAula.pack()
        self.frameProfessor.pack()
        self.frameNumeroAulas.pack()
        self.frameButton.pack()

        # CPF
        self.labelcpf = tk.Label(self.framecpfAluno, text="Informe o CPF: ")
        self.labelcpf.pack(side="left")
        self.inputcpfAluno = tk.Entry(self.framecpfAluno, width=30)
        self.inputcpfAluno.pack(side="left")

        # Nome
        self.labelnome = tk.Label(self.framenomeAluno, text="Informe o Nome: ")
        self.labelnome.pack(side="left")
        self.inputnomeAluno = tk.Entry(self.framenomeAluno, width=30)
        self.inputnomeAluno.pack(side="left")

        # Email
        self.labelemail = tk.Label(self.frameemailAluno, text="Informe o Email: ")
        self.labelemail.pack(side="left")
        self.inputemailAluno = tk.Entry(self.frameemailAluno, width=30)
        self.inputemailAluno.pack(side="left")

        # Tipo de Aula
        self.labelTipoAula = tk.Label(self.frameTipoAula, text="Escolha o Tipo de Aula: ")
        self.labelTipoAula.pack(side="left")
        tipoAula = ["Pilates", "Treino Funcional"]
        self.inputTipoAula = ttk.Combobox(self.frameTipoAula, values=tipoAula, state="readonly")
        self.inputTipoAula.pack(side="left")

        # Professor
        self.labelProfessor = tk.Label(self.frameProfessor, text="Escolha o Professor: ")
        self.labelProfessor.pack(side="left")
        self.inputNomeProfessor = ttk.Combobox(self.frameProfessor, width=30, state="readonly")
        self.inputNomeProfessor['values'] = listaProfessores  # Preenchendo com os nomes dos professores
        self.inputNomeProfessor.pack(side="left")

        # Número de Aulas
        self.labelNumeroAulas = tk.Label(self.frameNumeroAulas, text="Número de Aulas por Semana: ")
        self.labelNumeroAulas.pack(side="left")
        nroAula = [2, 3, 4]
        self.inputNroAulaSemanais = ttk.Combobox(self.frameNumeroAulas, values=nroAula, state="readonly")
        self.inputNroAulaSemanais.pack(side="left")

        # Botões
        self.buttonCria = tk.Button(self.frameButton, text="Cadastrar Aluno")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaAluno)

        self.buttonFecha = tk.Button(self.frameButton, text="Fechar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", lambda e: self.destroy())

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlAluno:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAluno = []

    def insereAluno(self):        
        listaNome = self.ctrlPrincipal.ctrlProfissional.getListaNome()
        self.limiteIns = LimiteInsereAluno(self, listaNome)
        self.limiteIns.mainloop()

    def criaAluno(self, event):
        cpf = self.limiteIns.inputcpfAluno.get()
        nome = self.limiteIns.inputnomeAluno.get()
        email = self.limiteIns.inputemailAluno.get()

        tipo_aula = self.limiteIns.inputTipoAula.get()
        professor = self.limiteIns.inputNomeProfessor.get() 
        numero_aulas = int(self.limiteIns.inputNroAulaSemanais.get())

        aluno = Aluno(cpf, nome, email, tipo_aula, professor, numero_aulas)

        self.listaAluno.append(aluno)

        self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
        self.limiteIns.destroy()

    def procuraAluno(self, cpf):
        for aluno in self.listaAluno:
            if aluno.cpf == cpf:
                return aluno
        return None

    def calcula_mensalidade(self, aluno):
        # Verificar se o professor existe
        professor = self.ctrlPrincipal.ctrlProfissional.getProfissional(aluno.professor)
        
        if professor is None:
            messagebox.showwarning("Erro", f"Professor '{aluno.professor}' não encontrado.")
            return 0  
        
        valor_base = professor.pilates if aluno.tipo_aula == 'Pilates' else professor.treinoFuncional

        # Ajuste de custo por número de aulas
        if aluno.numero_aulas == 2:
            custo_professor = valor_base
        elif aluno.numero_aulas == 3:
            custo_professor = valor_base * 1.4
        elif aluno.numero_aulas == 4:
            custo_professor = valor_base * 1.8

        # Adiciona o custo do estúdio (50% sobre o custo do professor)
        custo_total = custo_professor * 1.5

        return custo_total

    def mostraAluno(self):
        cpf = simpledialog.askstring("Buscar Aluno", "Digite o CPF do aluno:")

        if cpf:
            aluno = self.procuraAluno(cpf)
            if aluno:
                mensalidade = self.calcula_mensalidade(aluno)

                mensagem = (
                    f"CPF do Aluno: {aluno.cpf}\n"
                    f"Nome: {aluno.nome}\n"
                    f"Email: {aluno.email}\n"
                    f"Tipo de Aula: {aluno.tipo_aula}\n"
                    f"Professor: {aluno.professor}\n"
                    f"Número de Aulas Semanais: {aluno.numero_aulas}\n"
                    f"Mensalidade: R${mensalidade:.2f}"
                )
                messagebox.showinfo("Aluno Encontrado", mensagem)
            else:
                messagebox.showwarning("Não Encontrado", f"Aluno com CPF '{cpf}' não encontrado.")