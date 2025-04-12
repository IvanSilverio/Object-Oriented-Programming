import tkinter as tk
import produtos as est
import cupom as trm

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)     

        self.produtoMenu.add_command(label="Cadastrar", command=self.controle.insereProdutos)
        self.produtoMenu.add_command(label="Consultar", command=self.controle.mostraProdutos)
        self.menubar.add_cascade(label="Produto", menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar", command=self.controle.insereCupom)  
        self.cupomMenu.add_command(label="Consultar", command=self.controle.mostraCupom)                           
        self.menubar.add_cascade(label="Cupom Fiscal", menu=self.cupomMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = est.CtrlProduto()
        self.ctrlCupom = trm.CtrlCupom(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProdutos(self):
        self.ctrlProduto.insereProdutos()

    def mostraProdutos(self):
        self.ctrlProduto.mostraProdutos()

    def insereCupom(self):
        self.ctrlCupom.insereCupom()

    def mostraCupom(self):
        self.ctrlCupom.mostraCupom()

if __name__ == '__main__':
    c = ControlePrincipal()