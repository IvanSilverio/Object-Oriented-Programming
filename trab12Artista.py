from tkinter import simpledialog, messagebox

class CtrlArtista:
    def __init__(self):
        self.artistas = {}

    def cadastraArtista(self):
        nome = simpledialog.askstring("Cadastrar Artista", "Digite o nome do artista:")
        if nome:
            if nome not in self.artistas:
                self.artistas[nome] = []  # Cada artista terá uma lista de álbuns
                messagebox.showinfo("Sucesso", f"Artista '{nome}' cadastrado com sucesso!")
            else:
                messagebox.showwarning("Erro", f"Artista '{nome}' já está cadastrado!")

    def consultaArtista(self):
        nome = simpledialog.askstring("Consultar Artista", "Digite o nome do artista:")
        if nome in self.artistas:
            albuns = self.artistas[nome]
            if albuns:
                detalhes = f"Artista: {nome}\n"
                for album in albuns:
                    detalhes += f"Álbum: {album['titulo']} ({album['ano']})\n"
                    for musica in album['musicas']:
                        detalhes += f"  - {musica}\n"
                messagebox.showinfo("Álbuns e Faixas", detalhes)
            else:
                messagebox.showinfo("Álbuns e Faixas", f"Artista: {nome}\nNenhum álbum cadastrado.")
        else:
            messagebox.showwarning("Erro", f"Artista '{nome}' não encontrado!")
