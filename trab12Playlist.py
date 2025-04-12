import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class CtrlPlaylist:
    def __init__(self, controle):
        self.controle = controle
        self.playlists = {}  # Dicionário de playlists, cada playlist contém uma lista de músicas
        self.artistas = controle.ctrlArtista.artistas  # Dicionário de artistas compartilhado

    def cadastraPlaylist(self):
        janela = tk.Toplevel(self.controle.root)
        janela.title("Cadastrar Playlist")
        janela.geometry("400x400")

        # Entrada do nome da playlist
        tk.Label(janela, text="Digite o nome da playlist:").pack(pady=5)
        nome_entry = tk.Entry(janela, width=30)
        nome_entry.pack(pady=5)

        # Seleção do artista
        tk.Label(janela, text="Selecione o artista:").pack(pady=5)
        artistas = list(self.artistas.keys())
        artista_cb = ttk.Combobox(janela, values=artistas, state="readonly")
        artista_cb.pack(pady=5)

        # Listbox para exibir músicas do artista selecionado
        tk.Label(janela, text="Músicas disponíveis:").pack(pady=5)
        musicas_lb = tk.Listbox(janela, height=10, width=40)
        musicas_lb.pack(pady=5)

        # Atualiza o listbox ao selecionar um artista
        def atualizarMusicas(event):
            artista = artista_cb.get()
            musicas_lb.delete(0, tk.END)
            if artista in self.artistas:
                for album in self.artistas[artista]:
                    for musica in album['musicas']:
                        musicas_lb.insert(tk.END, musica)

        artista_cb.bind("<<ComboboxSelected>>", atualizarMusicas)

        # Lista de músicas selecionadas
        tk.Label(janela, text="Músicas adicionadas:").pack(pady=5)
        adicionadas_lb = tk.Listbox(janela, height=10, width=40)
        adicionadas_lb.pack(pady=5)

        # Adiciona a música selecionada no listbox ao playlist
        def adicionarMusica():
            musica = musicas_lb.get(tk.ACTIVE)
            if musica:
                adicionadas_lb.insert(tk.END, musica)

        tk.Button(janela, text="Adicionar Música", command=adicionarMusica).pack(pady=5)

        # Salvar a playlist
        def salvarPlaylist():
            nome = nome_entry.get()
            if nome:
                if nome not in self.playlists:
                    musicas = adicionadas_lb.get(0, tk.END)
                    self.playlists[nome] = list(musicas)
                    messagebox.showinfo("Sucesso", f"Playlist '{nome}' cadastrada com sucesso!")
                    janela.destroy()
                else:
                    messagebox.showwarning("Erro", f"Playlist '{nome}' já existe!")
            else:
                messagebox.showwarning("Erro", "O nome da playlist não pode ser vazio!")

        tk.Button(janela, text="Salvar Playlist", command=salvarPlaylist).pack(pady=10)

    def consultaPlaylist(self):
        nome = simpledialog.askstring("Consultar Playlist", "Digite o nome da playlist:")
        if nome in self.playlists:
            musicas = self.playlists[nome]
            musicas_str = "\n".join(musicas) if musicas else "Nenhuma música cadastrada."
            messagebox.showinfo("Playlist", f"Nome: {nome}\nMúsicas:\n{musicas_str}")
        else:
            messagebox.showwarning("Erro", f"Playlist '{nome}' não encontrada!")
