import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

class Aluno:
    def __init__(self, cpf, nome, email, tipoAula, nomeProfessor, nroAulaSemanais):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__tipoAula = tipoAula
        self.__nomeProfessor = nomeProfessor
        self.__nroAulasSemanais = nroAulaSemanais

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
    def tipoAula(self):
        return self.__tipoAula
    
    @property
    def nomeProfessor(self):
        return self.__nomeProfessor
    
    @property
    def nroAulaSemanais(self):
        return self.__nroAulasSemanais
    
class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaNome):

        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Aluno")
        self.controle = controle

        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.frameTipoAula = tk.Frame(self)
        self.frameNomeProfessor = tk.Frame(self)
        self.frameNroAulaSemanais = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.frameTipoAula.pack()
        self.frameNomeProfessor.pack()
        self.frameNroAulaSemanais.pack()
        self.frameButton.pack()
      
        self.labelCpf = tk.Label(self.framecpf,text="CPF: ")
        self.labelNome = tk.Label(self.framenome,text="Nome: ")
        self.labelEmail = tk.Label(self.frameemail, text='Email: ')
        self.labelTipoAula = tk.Label(self.frameTipoAula, text="Tipo da aula: ")
        self.labelNomeProfessor = tk.Label(self.frameNomeProfessor, text="Nome do professor: ")
        self.labelNroAulaSemanais = tk.Label(self.frameNroAulaSemanais, text="Número de aulas semanais: ")
        self.labelCpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelTipoAula.pack(side="left")
        self.labelNroAulaSemanais.pack(side="left")
        self.labelNomeProfessor.pack(side="left")

        self.inputCPF = tk.Entry(self.framecpf, width=20)
        self.inputCPF.pack(side="left")

        self.inputNome = tk.Entry(self.framenome, width=20)
        self.inputNome.pack(side="left")

        self.inputEmail = tk.Entry(self.frameemail, width=20)
        self.inputEmail.pack(side="left")

        tipoAula = ["Pilates", "Treino funcional"]
        self.inputTipoAula = ttk.Combobox(self.frameTipoAula, values=tipoAula, state="readonly")
        self.inputTipoAula.pack(side="left")

        self.escolhaCombo = tk.StringVar()
        self.inputNomeProfessor = ttk.Combobox(self.frameNomeProfessor, width = 15 , textvariable = self.escolhaCombo)
        self.inputNomeProfessor.pack(side="left")
        self.inputNomeProfessor['values'] = listaNome

        nroAula = [2, 3, 4]
        self.inputNroAulaSemanais = ttk.Combobox(self.frameNroAulaSemanais, values=nroAula, state="readonly")
        self.inputNroAulaSemanais.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAluno():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class CtrlAluno():       
    def __init__(self, controle):
        self.ctrlPrincipal = controle
        self.listaAluno = [
            Aluno('444.444.444-44', 'Carlos', 'carlos@gmail.com', 'Pilates', 'Pedro', 2),
            Aluno('555.555.555-55', 'Raquel', 'Raquel@gmail.com', 'Treino funcional', 'Joao', 3),
            Aluno('666.666.666-66', 'Alan', 'Alan@gmail.com', 'Pilates', 'Maria', 4)
        ]

    def getAluno(self, nome):
        estRet = None
        for est in self.listaAluno:
            if est.nome == nome:
                estRet = est
        return estRet

    def getListaCodigo(self):
        self.listaNome = []
        for est in self.listaAluno:
            self.listaNome.append(est.nome)
        return self.listaNome

    def insereAluno(self):
        listaNome = self.ctrlPrincipal.ctrlProfissional.getListaNome()
        self.limiteIns = LimiteInsereAluno(self, listaNome)

    def ProcuraAluno(self, cpf):
        for aluno in self.listaAluno:
            if cpf == aluno.cpf:
                return aluno
        return None

    def getValor(self):
        i = 0
        valor = self.ctrlPrincipal.ctrlProfissional.listaValor()
        for valorAluno in self.listaAluno:
            if valor[i] == valorAluno.nome[i]:
                return valor[i]
            i += 1
        

    def mostraAluno(self):
        cpf = simpledialog.askstring("Buscar Aluno", "Digite o cpf do aluno:")
        if cpf:
            aluno = self.ProcuraAluno(cpf)
            if aluno:
                    listaProfissionais = self.ctrlPrincipal.ctrlProfissional.listaProfissionais
                    for profs in listaProfissionais:
                        if profs.nome == aluno.nomeProfessor:
                            if aluno.tipoAula == "Pilates":
                                total = profs.valorPilates
                            elif aluno.tipoAula == "Treino funcional":
                                total = profs.valorTreinoFunc
                            else:
                                total = 0
                    if aluno.nroAulaSemanais == 3:
                        total += (total * 0.4)
                    elif aluno.nroAulaSemanais == 4:
                        total += (total + 0.8)
                    else:
                        total
            
                    messagebox.showinfo("Aluno encontrado",
                                            f"CPF: {aluno.cpf}\n"
                                            f"Nome: {aluno.nome}\n"
                                            f"Email: {aluno.email}\n"
                                            f"Tipo da aula: {aluno.tipoAula}\n"
                                            f"Nome do Professor: {aluno.nomeProfessor}\n"
                                            f"Número de aulas semanais: {aluno.nroAulaSemanais}\n"
                                            f"Valor da mensalidade: R$ {(total / 2) + total:.2f}\n"
                                        )
            else:
                messagebox.showwarning("Não Encontrado", f"Produto com código '{aluno}' não encontrado.")

    def enterHandler(self, event):
        cpf = self.limiteIns.inputCPF.get()
        nome = self.limiteIns.inputNome.get()
        email = self.limiteIns.inputEmail.get()
        tipoAula = self.limiteIns.inputTipoAula.get()
        nomeProfessor = self.limiteIns.inputNomeProfessor.get()
        nroAulaSemanais = self.limiteIns.inputNroAulaSemanais.get()
        profissionais = Aluno(cpf, nome, email, tipoAula, nomeProfessor, nroAulaSemanais)
        self.listaAluno.append(profissionais)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
        self.clearHandler(event)


    def clearHandler(self, event):
        self.limiteIns.inputCPF.delete(0, len(self.limiteIns.inputCPF.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputTipoAula.delete(0, len(self.limiteIns.inputTipoAula.get()))
        self.limiteIns.inputNomeProfessor.delete(0, len(self.limiteIns.inputNomeProfessor.get()))
        self.limiteIns.inputNroAulaSemanais.delete(0, len(self.limiteIns.inputNroAulaSemanais.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()