import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Comanda:
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__listaProd = []
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def listaProd(self):
        return self.__listaProd

    def addItem(self, item):
        self.__listaProd.append(item)

    def getComanda(self):
        msg = "Código: " + str(self.codigo) + "\n-------------------------" + "\nProdutos: "
        soma = 0
        for prod in self.listaProd:
            msg += "\nCódigo: " + str(prod[0].codigo)\
            + "\nDescrição: " + str(prod[0].desc)\
            + "\nPreço: " + str(prod[0].valor)\
            + "\nQuantidade: " + str(prod[1])\
            + "\n"
            soma += float(prod[0].valor)*prod[1]

        msg += "\nValor total: " + str(soma)
        return msg
    
class Produto:
    def __init__(self, codigo, desc, valor):
        self.__codigo = codigo
        self.__desc = desc
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def desc(self):
        return self.__desc
    
    @property
    def valor(self):
        return self.__valor

class LimiteInsereComanda(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Lançar Comanda")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameQuant = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameProduto.pack()
        self.frameQuant.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelProduto = tk.Label(self.frameProduto,text="Produto: ")
        self.labelQuant = tk.Label(self.frameQuant, text="Quantidade: ")

        self.labelCodigo.pack(side="left")
        self.labelProduto.pack(side="left")
        self.labelQuant.pack(side="left")

        listaProduto = []
        for prod in self.controle.listaProduto:
            listaProduto.append(prod.desc)

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.escolhaProd = tk.StringVar()
        self.comboboxProd = ttk.Combobox(self.frameProduto, width = 15 ,values=listaProduto, textvariable = self.escolhaProd)
        self.inputQuant = tk.Entry(self.frameQuant, width=20)

        self.inputCodigo.pack(side="left")
        self.comboboxProd.pack(side="left")
        self.inputQuant.pack(side="left")
      
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

class LimiteImprimeComanda(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Imprimir Comanda")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")

        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)

        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterImpHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaImpHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlComanda():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaComandas = []

        self.listaProduto = [
            Produto(901,'Refeicao',40),
            Produto(902,'Refeicao Crianca',20),
            Produto(903,'Guarana lata',6),
            Produto(904,'Coca Cola lata',6),
            Produto(905,'Suco laranja 400ml',8),
            Produto(906,'Cerveja Heineken lata',8),
            Produto(907,'Agua mineral 500ml',4),
            Produto(908,'Sorvete Kibon',8),
            Produto(909,'Chocolate Alpino',6),
            Produto(910,'Chocolate Lacta',5)
        ] 
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def getProd(self, desc):
        for prod in self.listaProduto:
            if prod.desc == desc:
                prodRet = prod
        return prodRet

    def lancaCom(self):
        self.limiteIns = LimiteInsereComanda(self)

    def imprimeCom(self):
        self.limiteImp = LimiteImprimeComanda(self)

    def calcFat(self):
        totalFatRef = 0
        totalFatProd = 0

        for com in self.listaComandas:
            for prod in com.listaProd:
                if prod[0].codigo == 901 or prod[0].codigo == 902:
                    totalFatRef += float(prod[0].valor)*prod[1]
                else:
                    totalFatProd += float(prod[0].valor)*prod[1]

        msg = "\nTotal Refeições: " + str(totalFatRef)\
            + "\nTotal Produtos: " + str(totalFatProd)\
            + "\n" \
            + "\nTotal Faturado: " + str(totalFatProd+totalFatRef)

        self.mostraJanela('Faturamento', msg)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        produtoDesc = self.limiteIns.comboboxProd.get()
        quant = int(self.limiteIns.inputQuant.get())

        produto = self.getProd(produtoDesc)

        aux = False

        for com in self.listaComandas:
            if com.codigo == codigo:
                #já existe uma comanda aberta
                for prod in com.listaProd:
                    if prod[0].codigo == produto.codigo:
                        #produto existe na comanda, adicionar quantidade
                        prod[1] += quant
                        aux = True
                if aux == False:
                    #produto não existe na comanda, adicionar produto
                    com.addItem([produto, quant])                        
                    aux = True
        if aux == False:
            #comanda não existe, devemos criá-la e adicionar o produto
            com = Comanda(codigo)
            com.addItem([produto, quant])                
            self.listaComandas.append(com)            
        self.limiteIns.mostraJanela('Sucesso', 'Comanda cadastrada/atualizada com sucesso')
        self.clearHandler(event)


    def enterImpHandler(self, event):
        codigo = self.limiteImp.inputCodigo.get()

        for com in self.listaComandas:
            if com.codigo == codigo:
                msg = com.getComanda()  
                self.limiteImp.mostraJanela('Comanda', msg)
                return

        self.limiteImp.mostraJanela('Erro', 'Código não cadastrado')               
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.comboboxProd.delete(0, len(self.limiteIns.comboboxProd.get()))
        self.limiteIns.inputQuant.delete(0, len(self.limiteIns.inputQuant.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def fechaImpHandler(self, event):
        self.limiteImp.destroy()