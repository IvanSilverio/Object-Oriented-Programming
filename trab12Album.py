from tkinter import simpledialog, messagebox

class CtrlAlbum:
    def __init__(self, controle):
        self.controle = controle
        self.albuns = {}  # Dicionário de álbuns
        self.artistas = controle.ctrlArtista.artistas  # Referência ao dicionário de artistas

    def cadastraAlbum(self):
        # Perguntar o nome do artista primeiro
        artista_nome = simpledialog.askstring("Cadastrar Álbum", "Digite o nome do artista:")
        if not artista_nome:
            messagebox.showwarning("Erro", "O nome do artista não pode ser vazio!")
            return

        # Verificar se o artista existe
        if artista_nome not in self.artistas:
            messagebox.showwarning("Erro", f"Artista '{artista_nome}' não encontrado!")
            return

        # Perguntar o título do álbum
        titulo = simpledialog.askstring("Cadastrar Álbum", "Digite o título do álbum:")
        if not titulo:
            messagebox.showwarning("Erro", "O título do álbum não pode ser vazio!")
            return

        # Verificar duplicidade do álbum
        if titulo in self.albuns:
            messagebox.showwarning("Erro", f"Álbum '{titulo}' já está cadastrado!")
            return

        # Perguntar o ano do álbum
        ano = simpledialog.askinteger("Cadastrar Álbum", "Digite o ano do álbum:")
        if not ano:
            messagebox.showwarning("Erro", "O ano do álbum não pode ser vazio!")
            return

        # Criar o álbum e adicionar ao dicionário
        novo_album = {'titulo': titulo, 'ano': ano, 'artista': artista_nome, 'musicas': []}
        self.albuns[titulo] = novo_album
        self.artistas[artista_nome].append(novo_album)  # Adicionar o álbum ao artista

        messagebox.showinfo("Sucesso", f"Álbum '{titulo}' cadastrado com sucesso para o artista '{artista_nome}'!")

        # Perguntar sobre músicas do álbum
        while True:
            musica_titulo = simpledialog.askstring("Cadastrar Música", "Digite o título da música (ou deixe vazio para finalizar):")
            if not musica_titulo:
                break  # Finalizar a inclusão de músicas
            novo_album['musicas'].append(musica_titulo)

        messagebox.showinfo("Sucesso", f"Álbum '{titulo}' finalizado com {len(novo_album['musicas'])} música(s)!")

    def consultaAlbum(self):
        # Perguntar o título do álbum
        titulo = simpledialog.askstring("Consultar Álbum", "Digite o título do álbum:")
        if titulo in self.albuns:
            album = self.albuns[titulo]
            musicas = album['musicas']
            musicas_str = "\n".join(musicas) if musicas else "Nenhuma música cadastrada."
            messagebox.showinfo("Álbum", f"Título: {titulo}\nArtista: {album['artista']}\nAno: {album['ano']}\nMúsicas:\n{musicas_str}")
        else:
            messagebox.showwarning("Erro", f"Álbum '{titulo}' não encontrado!")
