import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.art = []

    def handle_create_graph(self, e):
        n_alb = self._view.txtNumAlbumMin.value
        self.art = self._model.load_art_filt(n_alb)
        self._view.txt_result.controls.clear()
        n_nodi = self._model.num_nodi()
        n_archi = self._model.num_edges()
        self._view.txt_result.controls.append(ft.Text(f'Grafo creato: {n_nodi} nodi (artisti),Archi: {n_archi}'))

        for a in self.art:
            self._view.ddArtist.options.append(ft.dropdown.Option(key=a.id,text=a.name))#riucorda passi valore come id
        self._view.ddArtist.disabled = False
        self._view.btnArtistsConnected.disabled = False
        self._view.update_page()

    def handle_connected_artists(self, e):
        art = self._view.ddArtist.value
        elenco_v = self._model.vicini(art)
        self._view.btnArtistsConnected.value = False

        for v in elenco_v:
            self._view.txt_result.controls.append(ft.Text(f'{v[0]}: {v[1]}')) #perche la funzione in model dorebbe essere una tupla
        self._view.update_page()


