import tkinter as tk
import trab12Artista as art
import trab12Album as alb
import trab12Playlist as pl

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)

        # Menu Artista
        self.artistaMenu = tk.Menu(self.menubar)
        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.cadastraArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        # Menu Álbum
        self.albumMenu = tk.Menu(self.menubar)
        self.albumMenu.add_command(label="Cadastrar", command=self.controle.cadastraAlbum)
        self.albumMenu.add_command(label="Consultar", command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        # Menu Playlist
        self.playlistMenu = tk.Menu(self.menubar)
        self.playlistMenu.add_command(label="Cadastrar", command=self.controle.cadastraPlaylist)
        self.playlistMenu.add_command(label="Consultar", command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)


class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = pl.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Gerenciador de Músicas")
        self.root.mainloop()

    def cadastraArtista(self):
        self.ctrlArtista.cadastraArtista()

    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()

    def cadastraAlbum(self):
        self.ctrlAlbum.cadastraAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def cadastraPlaylist(self):
        self.ctrlPlaylist.cadastraPlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()
