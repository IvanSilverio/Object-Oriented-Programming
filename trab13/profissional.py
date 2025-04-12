import tkinter as tk
from tkinter import simpledialog, messagebox

class Profissional:
    def __init__(self, cpf, nome, email, pilates, treinoFuncional):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__pilates = pilates
        self.__treinoFuncional = treinoFuncional

    @property
    def pilates(self):
        return self.__pilates
    
    @property
    def treinoFuncional(self):
        return self.__treinoFuncional

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email

class LimiteInsereProfissional(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Profissional")
        self.controle = controle

        # Frames
        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framepilates = tk.Frame(self)
        self.frametreinoFuncional = tk.Frame(self)

        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.framepilates.pack()
        self.frametreinoFuncional.pack()
        self.frameButton.pack()

        # Labels
        self.labelcpf = tk.Label(self.framecpf, text="CPF: ")
        self.labelnome = tk.Label(self.framenome, text="Nome: ")
        self.labelemail = tk.Label(self.frameemail, text='Email: ')
        self.labelpilates = tk.Label(self.framepilates, text='Valor do Pilates: ')
        self.labeltreinoFuncional = tk.Label(self.frametreinoFuncional, text='Valor do Treino Funcional: ')

        # Posicionar as Labels
        self.labelcpf.pack(side="left")
        self.labelnome.pack(side="left")
        self.labelemail.pack(side="left")  
        self.labelpilates.pack(side="left")  
        self.labeltreinoFuncional.pack(side="left")

        # Inputs
        self.inputcpf = tk.Entry(self.framecpf, width=20)
        self.inputcpf.pack(side="left")
        self.inputNome = tk.Entry(self.framenome, width=20)
        self.inputNome.pack(side="left")
        self.inputEmail = tk.Entry(self.frameemail, width=20)
        self.inputEmail.pack(side="left")  
        self.inputPilates = tk.Entry(self.framepilates, width=20)
        self.inputPilates.pack(side="left")
        self.inputtreinoFuncional = tk.Entry(self.frametreinoFuncional, width=20)
        self.inputtreinoFuncional.pack(side="left")         

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton, text="Limpar")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton, text="Fechar")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraProfissional():
    def __init__(self, str):
        messagebox.showinfo('Lista dos Profissionais', str)

class CtrlProfissional():
    def __init__(self, ctrlAluno):  
        self.listaProfissional = []
        self.ctrlAluno = ctrlAluno  

    def getListaNome(self):
        lista_nome = []
        for prof in self.listaProfissional:
            lista_nome.append(prof.nome)
        return lista_nome

    def getProfissional(self, cpf):
        profRet = None
        for prof in self.listaProfissional:
            if prof.cpf == cpf:
                profRet = prof
        return profRet

    def getListaCodigo(self):
        listaCod = []
        for prof in self.listaProfissional:
            listaCod.append(prof.cpf)
        return listaCod
    
    def procurarProfissional(self, cpf):
        for produto in self.listaProfissional:
            if produto.cpf == cpf:
                return produto
        return None
    
    def calcula_mensalidade(self, numero_aulas, valor_base):
        # Ajuste de custo por número de aulas
        if numero_aulas == 2:
            custo_professor = valor_base
        elif numero_aulas == 3:
            custo_professor = valor_base * 1.4
        elif numero_aulas == 4:
            custo_professor = valor_base * 1.8
        else:
            raise ValueError("Número de aulas inválido")

        # Custo total com 50% adicional para o estúdio
        custo_total = custo_professor * 1.5
        return custo_total

    def insereProfissional(self):
        self.limiteIns = LimiteInsereProfissional(self) 

    def faturamentoProfissional(self):
        cpf = simpledialog.askstring("Buscar Profissional", "Digite o CPF do profissional:")

        if cpf:
            profissional = self.procurarProfissional(cpf)
            if profissional:
                alunos_pilates = []
                alunos_funcional = []

                # Construir listas de alunos por tipo de aula
                for aluno in self.ctrlAluno.listaAluno:  
                    if aluno.professor == profissional.nome:
                        if aluno.tipo_aula == 'Pilates':
                            alunos_pilates.append(aluno)
                        elif aluno.tipo_aula == 'Treino Funcional':
                            alunos_funcional.append(aluno)

                # Calcular faturamento por tipo de aula
                faturamento_pilates = 0
                for aluno in alunos_pilates:
                    faturamento_pilates += aluno.numero_aulas * profissional.pilates

                faturamento_funcional = 0
                for aluno in alunos_funcional:
                    faturamento_funcional += aluno.numero_aulas * profissional.treinoFuncional

                mensagem = (
                    f"Faturamento do Profissional: {profissional.nome}\n\n"
                    f"Valor total de Pilates: R${faturamento_pilates:.2f}\n"
                    f"Valor total de Treino Funcional: R${faturamento_funcional:.2f}\n"
                    f"Faturamento Total: R${faturamento_pilates + faturamento_funcional:.2f}"
                )

                messagebox.showinfo("Faturamento", mensagem)
            else:
                messagebox.showwarning("Não Encontrado", f"Profissional com CPF '{cpf}' não encontrado.")
        else:
            messagebox.showwarning("Erro", "CPF não informado.")

    def mostraProfissional(self):
        str = 'CPF -- Nome -- Email -- Valor Pilates -- Valor Treino Funcional\n'
        for prof in self.listaProfissional:
            str += f"{prof.cpf} -- {prof.nome} -- {prof.email} -- R${prof.pilates:.2f} -- R${prof.treinoFuncional:.2f}\n"
        self.limiteLista = LimiteMostraProfissional(str)

    def enterHandler(self, event):
        cpf = str(self.limiteIns.inputcpf.get())
        nome = self.limiteIns.inputNome.get()
        email = self.limiteIns.inputEmail.get()
        pilates = float(self.limiteIns.inputPilates.get())
        treinoFuncional = float(self.limiteIns.inputtreinoFuncional.get())

        profissional = Profissional(cpf, nome, email, pilates, treinoFuncional)
        self.listaProfissional.append(profissional)
        self.limiteIns.mostraJanela('Sucesso', 'Profissional cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputcpf.delete(0, len(self.limiteIns.inputcpf.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputPilates.delete(0, len(self.limiteIns.inputPilates.get()))
        self.limiteIns.inputtreinoFuncional.delete(0, len(self.limiteIns.inputtreinoFuncional.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()