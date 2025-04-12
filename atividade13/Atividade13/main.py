import tkinter as tk
import profissinal as prof
import aluno as alu

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.profissionalMenu = tk.Menu(self.menubar)
        self.alunoMenu = tk.Menu(self.menubar)     

        self.profissionalMenu.add_command(label="Cadastrar", command=self.controle.insereProfissionais)
        self.profissionalMenu.add_command(label="Lista", command=self.controle.mostraProfissionais)
        self.profissionalMenu.add_command(label="Faturamento", command=self.controle.faturamentoProfissional)
        self.menubar.add_cascade(label="Profissonal", menu=self.profissionalMenu)

        self.alunoMenu.add_command(label="Cadastrar", command=self.controle.insereAluno)  
        self.alunoMenu.add_command(label="Consultar", command=self.controle.mostraAluno)                           
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)        
    
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProfissional = prof.CtrlProfissional(self)
        self.ctrlAluno = alu.CtrlAluno(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProfissionais(self):
        self.ctrlProfissional.insereProfissionais()

    def mostraProfissionais(self):
        self.ctrlProfissional.mostraProfissionais()

    def faturamentoProfissional(self):
        self.ctrlProfissional.faturamentoProfissional()

    def insereAluno(self):
        self.ctrlAluno.insereAluno()

    def mostraAluno(self):
        self.ctrlAluno.mostraAluno()

if __name__ == '__main__':
    c = ControlePrincipal()