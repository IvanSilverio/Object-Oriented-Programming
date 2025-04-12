import tkinter as tk
from tkinter import simpledialog, messagebox

class Produto:

    def __init__(self, codigo, descricao, valorUni):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUni = valorUni

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorUni(self):
        return self.__valorUni

class LimiteInsereProdutos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.framecod = tk.Frame(self)
        self.framedesc = tk.Frame(self)
        self.framevalor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framecod.pack()
        self.framedesc.pack()
        self.framevalor.pack()
        self.frameButton.pack()
      
        self.labelcod = tk.Label(self.framecod,text="Codigo produto: ")
        self.labeldesc = tk.Label(self.framedesc,text="Descricao: ")
        self.labelvalor = tk.Label(self.framevalor, text='Valor unitário: ')
        self.labelcod.pack(side="left")
        self.labeldesc.pack(side="left")
        self.labelvalor.pack(side="left")  

        self.inputCod = tk.Entry(self.framecod, width=20)
        self.inputCod.pack(side="left")
        self.inputDesc = tk.Entry(self.framedesc, width=20)
        self.inputDesc.pack(side="left")
        self.inputValor = tk.Entry(self.framevalor, width=20)
        self.inputValor.pack(side="left")           
      
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

class LimiteMostraProdutos():
    def __init__(self, str):
        messagebox.showinfo('Lista dos produtos', str)

      
class CtrlProduto():       
    def __init__(self):
        self.listaProdutos = [
            Produto('101', 'Coca-cola lata 350 ml', 10.50),
            Produto('102', 'Suco Del Valle 500 ml', 5.00),
            Produto('103', 'Salgadinho fandangos 100g', 7.50)
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
    
    def procurarProduto(self, codigo):
        for produto in self.listaProdutos:
            if produto.codigo == codigo:  # Comparação consistente
                return produto
        return None

    def insereProdutos(self):
        self.limiteIns = LimiteInsereProdutos(self) 

    def mostraProdutos(self):
        codigo = simpledialog.askstring("Buscar Produto", "Digite o código do produto:")

        if codigo:
            produto = self.procurarProduto(codigo)
            if produto:
                messagebox.showinfo("Produto Encontrado", f"Código: {produto.codigo}\nNome: {produto.descricao}\nValor Unitário: R${produto.valorUni:.2f}")
            else:
                messagebox.showwarning("Não Encontrado", f"Produto com código '{codigo}' não encontrado.")

    def enterHandler(self, event):
        codigo = str(self.limiteIns.inputCod.get())  # Converte para string
        descricao = self.limiteIns.inputDesc.get()
        valorUni = float(self.limiteIns.inputValor.get())  # Converte para float
        produtos = Produto(codigo, descricao, valorUni)
        self.listaProdutos.append(produtos)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)


    def clearHandler(self, event):
        self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
        self.limiteIns.inputDesc.delete(0, len(self.limiteIns.inputDesc.get()))
        self.limiteIns.inputValor.delete(0, len(self.limiteIns.inputValor.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    