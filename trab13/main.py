import tkinter as tk
import profissional as prof
import aluno as alu

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.alunoMenu = tk.Menu(self.menubar)     

        self.produtoMenu.add_command(label="Cadastrar", command=self.controle.insereProfissional)
        self.produtoMenu.add_command(label="Lista", command=self.controle.mostraProfissional)
        self.produtoMenu.add_command(label="Faturamento", command=self.controle.faturamentoProfissional)

        self.menubar.add_cascade(label="Profissional", menu=self.produtoMenu)

        self.alunoMenu.add_command(label="Cadastra", command=self.controle.insereAluno)  
        self.alunoMenu.add_command(label="Consulta", command=self.controle.mostraAluno)                           
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = alu.CtrlAluno(self)
        self.ctrlProfissional = prof.CtrlProfissional(self.ctrlAluno)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProfissional(self):
        self.ctrlProfissional.insereProfissional()

    def mostraProfissional(self):
        self.ctrlProfissional.mostraProfissional()

    def faturamentoProfissional(self):
        self.ctrlProfissional.faturamentoProfissional()

    def insereAluno(self):
        self.ctrlAluno.insereAluno()

    def mostraAluno(self):
        self.ctrlAluno.mostraAluno()

if __name__ == '__main__':
    c = ControlePrincipal()
