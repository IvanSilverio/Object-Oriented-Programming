import tkinter as tk
from tkinter import messagebox, simpledialog

class Profissional:
    def __init__(self, cpf, nome, email, valorPilates, valorTreinoFunc):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__valorPilates = valorPilates
        self.__valorTreinoFunc = valorTreinoFunc

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
    def valorPilates(self):
        return self.__valorPilates
    
    @property
    def valorTreinoFunc(self):
        return self.__valorTreinoFunc
    
class LimiteInsereProfissional(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Profissional")
        self.controle = controle

        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.frameValorPilates = tk.Frame(self)
        self.frameTreinoFunc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.frameValorPilates.pack()
        self.frameTreinoFunc.pack()
        self.frameButton.pack()
      
        self.labelCpf = tk.Label(self.framecpf,text="CPF: ")
        self.labelNome = tk.Label(self.framenome,text="Nome: ")
        self.labelEmail = tk.Label(self.frameemail, text='Email: ')
        self.labelValorPilates = tk.Label(self.frameValorPilates, text="Valor da aula de pilates: ")
        self.labelTreinoFunc = tk.Label(self.frameTreinoFunc, text="Valor da aula de treino funcional: ")
        self.labelCpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelValorPilates.pack(side="left")
        self.labelTreinoFunc.pack(side="left")

        self.inputCPF = tk.Entry(self.framecpf, width=20)
        self.inputCPF.pack(side="left")
        self.inputNome = tk.Entry(self.framenome, width=20)
        self.inputNome.pack(side="left")
        self.inputEmail = tk.Entry(self.frameemail, width=20)
        self.inputEmail.pack(side="left")  
        self.inputValorPilates = tk.Entry(self.frameValorPilates, width=20)
        self.inputValorPilates.pack(side="left")
        self.inputTreinoFunc = tk.Entry(self.frameTreinoFunc, width=20)
        self.inputTreinoFunc.pack(side="left")     
      
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

class LimiteMostraProfissional():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

class CtrlProfissional():       
    def __init__(self, controle):
        self.ctrlPrincipal = controle
        self.listaProfissionais = [
            Profissional('111.111.111-11', 'Pedro', 'pedro@gmail.com', 100, 200),
            Profissional('222.222.222-22', 'Joao', 'joao@gmail.com', 200, 100),
            Profissional('333.333.333-33', 'Maria', 'maria@gmail.com', 300, 400)
        ]

    def getProfissional(self, nome):
        estRet = None
        for est in self.listaProfissionais:
            if est.nome == nome:
                estRet = est
        return estRet

    def getListaNome(self):
        self.listaNome = []
        for est in self.listaProfissionais:
            self.listaNome.append(est.nome)
        return self.listaNome

    def insereProfissionais(self):
        self.limiteIns = LimiteInsereProfissional(self)

    def listaValor(self):
        listaValor = []
        for valor in self.listaProfissionais:
            total = 0
            total += valor.valorPilates + valor.valorTreinoFunc
            listaValor.append(total)
        return listaValor

    def mostraProfissionais(self):
        texto = ''
        for disc in self.listaProfissionais:
            texto += 'CPF - ' + disc.cpf + '\n'
            texto += 'Email - ' + disc.email + '\n'
            texto += 'Nome - ' + disc.nome + '\n'
            texto += 'Valor Pilates - ' + str(disc.valorPilates) + '\n'
            texto += 'Valor Treino Funcional - ' + str(disc.valorTreinoFunc) + '\n'+'\n'
        self.limiteLista = LimiteMostraProfissional(texto)

    def faturamentoProfissional(self):
        cpf = simpledialog.askstring("Faturamento", "Digite o CPF do profissional:")
        faturamento_pilates = 0
        faturamento_funcional = 0
        
        for profissional in self.listaProfissionais:
            if profissional.cpf == cpf:
                for aluno in self.ctrlPrincipal.ctrlAluno.listaAluno:
                    if aluno.nomeProfessor == profissional.nome:
                        # Calcular o faturamento com base no tipo de aula e número de aulas semanais
                        if aluno.tipoAula == "Pilates":
                            faturamento_pilates += profissional.valorPilates * aluno.nroAulaSemanais
                        elif aluno.tipoAula == "Treino funcional":
                            faturamento_funcional += profissional.valorTreinoFunc * aluno.nroAulaSemanais

                # Exibir faturamento separado por tipo de aula
                messagebox.showinfo("Faturamento", 
                                    f"Faturamento do profissional {profissional.nome}:\n"
                                    f"Pilates: R$ {faturamento_pilates:.2f}\n"
                                    f"Treino Funcional: R$ {faturamento_funcional:.2f}\n"
                                    f"Faturamento total: R$ {faturamento_pilates + faturamento_funcional:.2f}")

    
    def criaFaturamento(self):
        return self.faturamentoProfissional(self)

    def enterHandler(self, event):
        cpf = self.limiteIns.inputCPF.get()
        nome = self.limiteIns.inputNome.get()
        email = self.limiteIns.inputEmail.get()
        valorPilates = self.limiteIns.inputValorPilates.get()
        valorFunc = self.limiteIns.inputTreinoFunc.get()
        profissionais = Profissional(cpf, nome, email, valorPilates, valorFunc)
        self.listaProfissionais.append(profissionais)
        self.limiteIns.mostraJanela('Sucesso', 'Profissional cadastrado com sucesso')
        self.clearHandler(event)


    def clearHandler(self, event):
        self.limiteIns.inputCPF.delete(0, len(self.limiteIns.inputCPF.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputValorPilates.delete(0, len(self.limiteIns.inputValorPilates.get()))
        self.limiteIns.inputTreinoFunc.delete(0, len(self.limiteIns.inputTreinoFunc.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    