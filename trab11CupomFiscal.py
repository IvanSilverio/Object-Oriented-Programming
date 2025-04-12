import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Produto:
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = float(valorUnitario)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valorUnitario(self):
        return self.__valorUnitario


class CupomFiscal:
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__itensCupom = []  # Lista para armazenar os itens do cupom

    @property
    def codigo(self):
        return self.__codigo

    @property
    def itensCupom(self):
        return self.__itensCupom  # Método para acessar os itens do cupom

    def adicionaItem(self, produto):
        """Método para adicionar um produto ao cupom fiscal."""
        self.__itensCupom.append(produto)


class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle, listaNroCupom):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cupom")
        self.controle = controle

        self.frameCodCupom = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodCupom.pack()
        self.frameProduto.pack()
        self.frameButton.pack()

        self.labelCodCupom = tk.Label(self.frameCodCupom, text="Informe o código do cupom: ")
        self.labelCodCupom.pack(side="left")
        self.inputCodCupom = tk.Entry(self.frameCodCupom, width=20)
        self.inputCodCupom.pack(side="left")

        self.labelEst = tk.Label(self.frameProduto, text="Escolha o produto: ")
        self.labelEst.pack(side="left")
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        for nro in listaNroCupom:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton, text="Insere Produto")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereProduto)

        self.buttonCria = tk.Button(self.frameButton, text="Fechar cupom")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaCupons)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraCupons:
    def __init__(self, str):
        messagebox.showinfo('Consulta de cupons', str)


class CtrlCupomFiscal:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCupomFiscal = []  # Lista para armazenar cupons fiscais
        self.listaCodProdutos = []  # Lista de produtos inseridos

    def insereCupons(self):
        """Método para chamar a interface de inserção de cupons."""
        listaCodprod = self.ctrlPrincipal.ctrlProduto.getListaCodigo()
        self.limiteIns = LimiteInsereCupom(self, listaCodprod)

    def criaCupons(self, event):
        
        """Método para criar o cupom fiscal."""
        codCupom = self.limiteIns.inputCodCupom.get()
        if codCupom:  # Verifica se o código do cupom foi informado
            # Verificar se o cupom já existe
            cupomExistente = self.procuraCupomFiscal(codCupom)
            if not cupomExistente:
                # Cria o cupom fiscal e o adiciona à lista de cupons
                cupomFiscal = CupomFiscal(codCupom)
                self.listaCupomFiscal.append(cupomFiscal)  # Adiciona à lista de cupons
                self.limiteIns.mostraJanela('Sucesso', 'Cupom Fiscal criado com sucesso')
                self.limiteIns.destroy()
            else:
                self.limiteIns.mostraJanela('Erro', 'Cupom Fiscal já existe.')
        else:
            self.limiteIns.mostraJanela('Erro', 'Código do cupom não pode ser vazio.')




    def insereProduto(self, event):
        """Método para inserir um produto no cupom fiscal."""
        produtoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(produtoSel)  # Buscar o produto pela lista de códigos
        
        if produto:
            cupom = self.procuraCupomFiscal(self.limiteIns.inputCodCupom.get())
            if cupom:
                cupom.adicionaItem(produto)  # Adiciona o produto ao cupom fiscal
                self.limiteIns.mostraJanela('Sucesso', 'Produto inserido no cupom')
            else:
                self.limiteIns.mostraJanela('Erro', 'Cupom não encontrado')
        else:
            self.limiteIns.mostraJanela('Erro', 'Produto não encontrado')



    def procuraCupomFiscal(self, codigo):
        """Método para procurar um cupom fiscal pelo código."""
        for cupom in self.listaCupomFiscal:
            if cupom.codigo == codigo:
                return cupom
        return None  # Retorna None se o cupom não for encontrado


    def contaProduto(self, cupom, codigo):
        """Método para contar a quantidade de produtos no cupom."""
        cont = 0
        for item in cupom.itensCupom:
            if item.codigo == codigo:
                cont += 1
        return cont

    def consultaCupons(self, codigo):
        """Método para consultar cupons fiscais e mostrar os produtos contidos neles."""
        cupom = self.procuraCupomFiscal(codigo)
        if cupom:
            mensagem = f"Código do Cupom: {cupom.codigo}\nItens no Cupom:\n"
            produtos_processados = set()  # Para evitar contar o mesmo produto várias vezes
            for prod in cupom.itensCupom:
                if prod.codigo not in produtos_processados:
                    quantidade = self.contaProduto(cupom, prod.codigo)  # Passando o cupom para contar
                    mensagem += (
                        f"--- Quantidade: {quantidade}\n"
                        f"  Código Produto: {prod.codigo}\n"
                        f"  Descrição: {prod.descricao}\n"
                        f"  Valor: R${prod.valorUnitario * quantidade:.2f}\n\n"
                    )
                    produtos_processados.add(prod.codigo)
            messagebox.showinfo("Cupom Encontrado", mensagem)
        else:
            messagebox.showwarning("Não Encontrado", f"Cupom com código '{codigo}' não encontrado.")
