import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Produto():

    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorUnitario(self):
        return self.__valorUnitario

class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValor.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Código do cupom: ")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descrição: ")
        self.labelValor = tk.Label(self.frameValor, text="Valor unitário: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelValor.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")      
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton, text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlProduto():       
    def __init__(self):
        self.listaProdutos = [
            Produto('1001', 'Fone', 'R$20.00'),
            Produto('1002', 'Lápis', 'R$5.00'),
            Produto('1003', 'Carregador', 'R$15.00'),
            Produto('1004', 'Mouse', 'R$25.00')
        ]

    def getProduto(self, codigo):
        estRet = None
        for est in self.listaProdutos:
            if est.codigo == codigo:
                estRet = est
        return estRet

    def getListaCodigo(self):
        self.listaCod = []
        for est in self.listaProdutos:
            self.listaCod.append(est.codigo)
        return self.listaCod

    def insereProduto(self):
        self.limiteIns = LimiteCadastraProduto(self)

    def consultaProduto(self):
        codigo = simpledialog.askstring("Consulta Produto", "Digite o código do produto:")
        encontrado = False  
        for produto in self.listaProdutos:
            if produto.codigo == codigo: 
                mensagem = (f"Produto encontrado:\nCódigo: {produto.codigo}\nDescrição: {produto.descricao}\nValor Unitário: {produto.valorUnitario}")
                messagebox.showinfo("Produto Encontrado", mensagem)           
                encontrado = True
                break
        if encontrado == False: 
            self.limiteIns.mostraJanela("Erro", "Código não cadastrado.") 

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        descricao = self.limiteIns.inputDescricao.get()
        valor = self.limiteIns.inputValor.get()
        produto = Produto(codigo, descricao, valor)
        self.listaProdutos.append(produto)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputDescricao.delete(0, len(self.limiteIns.inputDescricao.get()))
        self.limiteIns.inputValor.delete(0, len(self.limiteIns.inputValor.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
