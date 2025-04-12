import tkinter as tk
import trab11Produto as prod
import trab11CupomFiscal as cupom
from tkinter import simpledialog



class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)     

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultaProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar", \
                    command=self.controle.insereCupons)  
        self.cupomMenu.add_command(label="Consulta", \
                    command=self.controle.consultaCupons)  # Corrigido aqui       
        self.menubar.add_cascade(label="Cupom Fiscal", \
                    menu=self.cupomMenu)        

        self.root.config(menu=self.menubar)


class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.CtrlProduto()
        self.ctrlCupomFiscal = cupom.CtrlCupomFiscal(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProduto(self):
        self.ctrlProduto.insereProduto()

    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()

    def insereCupons(self):
        self.ctrlCupomFiscal.insereCupons()

    def consultaCupons(self):
        # Solicitar o código do cupom ao usuário
        codigo = simpledialog.askstring("Buscar Cupom", "Digite o código do cupom:")
        if codigo:
            self.ctrlCupomFiscal.consultaCupons(codigo)  # Passar o código para a consulta


if __name__ == '__main__':
    c = ControlePrincipal()
