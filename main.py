import tkinter as tk
import comanda as com

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.comandaMenu = tk.Menu(self.menubar)

        self.comandaMenu.add_command(label="Lançar comanda", command=self.controle.lancaCom)
        self.comandaMenu.add_command(label="Imprimir comanda", command=self.controle.imprimeCom)
        self.comandaMenu.add_command(label="Calcular faturamento", command=self.controle.calcFat)
        self.menubar.add_cascade(label="Comanda", menu=self.comandaMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlComanda = com.CtrlComanda(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Comida Boa")
        # Inicia o mainloop
        self.root.mainloop()
    
    def lancaCom(self):
        self.ctrlComanda.lancaCom()

    def imprimeCom(self):
        self.ctrlComanda.imprimeCom()
    
    def calcFat(self):
        self.ctrlComanda.calcFat()

if __name__ == '__main__':
    c = ControlePrincipal()