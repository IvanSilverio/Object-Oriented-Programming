import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

class Cupom:

    def __init__(self, codigo, itensCupom):
        self.__codigo = codigo
        self.__itensCupom = itensCupom

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def itensCupom(self):
        return self.__itensCupom
    

class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle, listaCodigo):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Turma")
        self.controle = controle

        self.frameCodCupom = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodCupom.pack()
        self.frameProduto.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodCupom,text="Informe o código do cupom: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodCupom = tk.Entry(self.frameCodCupom, width=20)
        self.inputCodCupom.pack(side="left")
          
        self.labelProd = tk.Label(self.frameProduto,text="Escolha o produto: ")
        self.labelProd.pack(side="left") 
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        for nro in listaCodigo:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereProduto)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Cupom")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaCrupom)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraCupom():
    def __init__(self, str):
        messagebox.showinfo('Lista de cupons', str)

class CtrlCupom():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCupom = []   
        self.listaCodProdutos = []

    def insereCupom(self):        
        listaCodprod = self.ctrlPrincipal.ctrlProduto.getListaCodigo()
        self.limiteIns = LimiteInsereCupom(self, listaCodprod)

    def criaCrupom(self, event):
        codTurma = self.limiteIns.inputCodCupom.get()
        cupom = Cupom(codTurma, self.listaCodProdutos)
        self.listaCupom.append(cupom)
        self.limiteIns.mostraJanela('Sucesso', 'Cupom criado com sucesso')
        self.limiteIns.destroy()

    def insereProduto(self, event):
        produtoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(produtoSel)
        self.listaCodProdutos.append(produto)
        self.limiteIns.mostraJanela('Sucesso', 'Produto inserido')

    def procuraCupom(self, codigo):
        for cup in self.listaCupom:
            if cup.codigo == codigo:
                return cup
        return None

    def contaProduto(self, codigo):
        cont = 0
        for conta in self.listaCodProdutos:
            if conta.codigo == codigo:
                cont += 1
        return cont

    def mostraCupom(self):

        codigo = simpledialog.askstring("Buscar Cupom", "Digite o código do cupom:")

        if codigo:
            cupom = self.procuraCupom(codigo)
            if cupom:
                mensagem = f"Código do Cupom: {cupom.codigo}\n\nItens no Cupom:\n\n"

                produtos_processados = set()

                for prod in cupom.itensCupom:

                    if prod.codigo not in produtos_processados:
                        quantidade = self.contaProduto(prod.codigo)
                        mensagem += (
                            f"--- Quantidade: {quantidade}\n"
                            f"  Código Produto: {prod.codigo}\n"
                            f"  Descrição:            {prod.descricao}\n"
                            f"  Valor:                    R${prod.valorUni * quantidade:.2f}\n\n"
                        )
                        produtos_processados.add(prod.codigo)

                messagebox.showinfo("Cupom Encontrado", mensagem)
            else:
                messagebox.showwarning("Não Encontrado", f"Cupom com código '{codigo}' não encontrado.")