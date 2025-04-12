import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Jogo:
    def __init__(self, codigo, nome, console, genero, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.console = console
        self.genero = genero
        self.preco = preco
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, valor):
        self.consoles = ["Xbox", "Playstation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Genero inválida: {}".format(valor))
        else:
            self.__genero = valor 

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0 or valor > 500:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = valor

    def getJogo(self):
        return "Nome: " + str(object=self.nome)\
        + "\nCodigo: " + str(object=self.codigo)\
        + "\nConsole: " + str(object=self.console)\
        + "\nGenero: " + str(object=self.genero)\
        + "\nPreço: " + str(object=self.preco)
    

class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Genero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=15)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")
      
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

class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Consultar Jogos por Avaliação")
        self.controle = controle

        self.frameFiltro = tk.Frame(self)
        self.frameFiltro.pack()
        self.frameResultados = tk.Frame(self)
        self.frameResultados.pack()

        self.labelFiltro = tk.Label(self.frameFiltro, text="Selecione a avaliação: ")
        self.labelFiltro.pack(side="left")

        self.comboEstrelas = ttk.Combobox(
            self.frameFiltro, values=["1", "2", "3", "4", "5"], width=15)
        self.comboEstrelas.pack(side="left")
        self.comboEstrelas.bind("<<ComboboxSelected>>", controle.filtrarJogosHandler)

        self.textResultados = tk.Text(self.frameResultados, width=50, height=15, state="disabled")
        self.textResultados.pack()

    def mostrarJogos(self, jogos):
        self.textResultados.config(state="normal")
        self.textResultados.delete("1.0", tk.END)
        if len(jogos) > 0:
            for jogo in jogos:
                self.textResultados.insert(tk.END, jogo.getJogo() + "\n\n")
        else:
            self.textResultados.insert(tk.END, "Nenhum jogo encontrado para esta avaliação.\n")
        self.textResultados.config(state="disabled")


class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Avaliar Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNota = tk.Frame(self)
        self.frameNota.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputCodigo.pack(side="left")

        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelNota.pack(side="left")
        self.comboNota = ttk.Combobox(self.frameNota, values=["1", "2", "3", "4", "5"], width=5)
        self.comboNota.pack(side="left")

        self.buttonAvaliar = tk.Button(self.frameButton, text="Avaliar", command=self.avaliarJogo)
        self.buttonAvaliar.pack()

    def avaliarJogo(self):
        codigo = self.inputCodigo.get()
        nota = self.comboNota.get()
        self.controle.salvaAvaliacaoHandler(codigo, nota)


class CtrlJogo:
    def __init__(self):
        self.listaJogos = []
        self.avaliacoesJogos = {}  # Dicionário para armazenar avaliações de cada jogo

    def cadastraJogo(self):
        self.limiteIns = LimiteInsereJogo(self)

    def consultaJogo(self):
        self.limiteCons = LimiteConsultaJogo(self)

    def filtrarJogosHandler(self, event):
        estrelas_str = self.limiteCons.comboEstrelas.get()
        if estrelas_str == "":
            return
        if estrelas_str == "1":
            estrelas = 1
        elif estrelas_str == "2":
            estrelas = 2
        elif estrelas_str == "3":
            estrelas = 3
        elif estrelas_str == "4":
            estrelas = 4
        elif estrelas_str == "5":
            estrelas = 5
        jogos_filtrados = self.filtrarJogosPorEstrelas(estrelas)
        self.limiteCons.mostrarJogos(jogos_filtrados)

    def filtrarJogosPorEstrelas(self, estrelas):
        jogos_filtrados = []
        for jogo in self.listaJogos:
            if jogo.codigo in self.avaliacoesJogos:
                avaliacoes = self.avaliacoesJogos[jogo.codigo]
                soma = sum(avaliacoes)
                media = soma / len(avaliacoes)
                if (estrelas == 1 and 0 <= media <= 1) or \
                   (estrelas == 2 and 1 < media <= 2) or \
                   (estrelas == 3 and 2 < media <= 3) or \
                   (estrelas == 4 and 3 < media <= 4) or \
                   (estrelas == 5 and 4 < media <= 5):
                    jogos_filtrados.append(jogo)
        return jogos_filtrados


    def avaliaJogo(self):
        self.limiteAva = LimiteAvaliaJogo(self)

    def salvaAvaliacaoHandler(self, codigo, nota):
        try:
            nota = int(nota)
            for jogo in self.listaJogos:
                if jogo.codigo == codigo:
                    if codigo not in self.avaliacoesJogos:
                        self.avaliacoesJogos[codigo] = []
                    self.avaliacoesJogos[codigo].append(nota)
                    messagebox.showinfo("Sucesso", "Avaliação salva com sucesso!")
                    return
            messagebox.showerror("Erro", "Jogo não encontrado.")
        except ValueError as error:
            messagebox.showerror("Erro", str(error))

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        console = self.limiteIns.inputConsole.get()
        genero = self.limiteIns.inputGenero.get()
        preco = int(self.limiteIns.inputPreco.get())

        try:
            jogo = Jogo(codigo, nome, console, genero, preco)
            self.listaJogos.append(jogo)            
            self.limiteIns.mostraJanela('Sucesso', 'Jogo cadastrado com sucesso')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela('Erro', error)            
    

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()