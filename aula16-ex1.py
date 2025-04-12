import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Classe que representa o modelo de cliente, armazenando nome, email e código
class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome  # Atributo privado para o nome do cliente
        self.__email = email  # Atributo privado para o email do cliente
        self.__codigo = codigo  # Atributo privado para o código do cliente

    # Propriedades para acessar os atributos privados
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @property
    def codigo(self):
        return self.__codigo

# Classe que representa a visualização da interface do usuário
class View():
    def __init__(self, master, controller):
        self.controller = controller  # Controlador que lida com os eventos
        self.janela = tk.Frame(master)
        self.janela.pack()

        # Criação de três frames para organizar os campos de entrada e botões
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        # Labels e campos de entrada para Nome, Email e Código
        self.labelInfo1 = tk.Label(self.frame1, text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3, text="Código: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left") 
        self.labelInfo3.pack(side="left")  

        # Campos de entrada de texto
        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")  
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")           
        
        # Botão para salvar o cliente
        self.buttonSubmit = tk.Button(self.janela, text="Salva")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        # Botão para limpar os campos de entrada
        self.buttonClear = tk.Button(self.janela, text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)   

        # Botão para consultar um cliente pelo código
        self.buttonConsulta = tk.Button(self.janela, text="Consulta código")      
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controller.consultaHandler)         

    # Método para mostrar uma janela de mensagem
    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

# Classe que controla a lógica do programa e manipula eventos
class Controller():       
    def __init__(self):
        self.root = tk.Tk()  # Janela principal
        self.root.geometry('300x100')  # Define o tamanho da janela
        self.listaClientes = []  # Lista para armazenar os clientes

        # Cria a view passando referência da janela principal e do controlador
        self.view = View(self.root, self) 

        self.root.title("Trabalho 10")  # Define o título da janela
        self.root.mainloop()  # Inicia o loop principal da interface gráfica

    # Método para salvar um cliente na lista
    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get()  # Obtém o nome do campo de entrada
        emailCli = self.view.inputText2.get()  # Obtém o email do campo de entrada
        codigoCli = self.view.inputText3.get()  # Obtém o código do campo de entrada
        cliente = ModelCliente(nomeCli, emailCli, codigoCli)  # Cria um novo cliente
        self.listaClientes.append(cliente)  # Adiciona o cliente à lista
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')  # Mostra mensagem de sucesso
        self.clearHandler(event)  # Limpa os campos de entrada

    # Método para limpar os campos de entrada
    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))  # Limpa o campo de nome
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))  # Limpa o campo de email
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))  # Limpa o campo de código

    # Método para consultar um cliente pelo código
    def consultaHandler(self, event):
        codigo = simpledialog.askstring("Consulta Cliente", "Digite o código do cliente:")  # Solicita o código
        encontrado = False  # Flag para verificar se o cliente foi encontrado
        for cliente in self.listaClientes:  # Percorre a lista de clientes
            if cliente.codigo == codigo:  # Verifica se o código coincide
                mensagem = (f"Cliente encontrado:\nNome: {cliente.nome}\nEmail: {cliente.email}")
                self.view.mostraJanela("Cliente Encontrado", mensagem)  # Exibe informações do cliente
                encontrado = True
                break
        if encontrado == False:  # Se o cliente não foi encontrado
            self.view.mostraJanela("Erro", "Código não cadastrado.")  # Exibe mensagem de erro

# Inicia o programa
if __name__ == '__main__':
    c = Controller()
