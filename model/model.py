import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.id_map = {}



    def load_art_filt(self,n_alb:int):
        self._artists_list = DAO.get_artisti_filtrati(n_alb)
        for a in self._artists_list:
            self.id_map[a.id] = a
        return self._artists_list

    def build_graph(self):
        #creazione grafo con i nodi ovvero gli artisti filtrati
        self._graph.clear()
        for a in self._artists_list: #aggiunta di tutti i nodi
            self._graph.add_node(a)
        #avendo archi a1,a2,peso
        tmp_ed = DAO.get_collegamenti()
        for e in tmp_ed:
            s1 = self.id_map[e.id]
            s2 = self.id_map[e.id]
            if s1 in self.id_map.keys() and s2 in self.id_map.keys(): # verifica se i due artisti appartengono agli artisti filtrati
                self._graph.add_edge(s1,s2,weight=e.peso)

    def vicini(self,art):
        risultati = []
        for v in self._graph.neighbors(art):
            peso = self._graph[art][v]['weight']
            risultati.append((v,peso))

        return sorted(risultati, key=lambda x: x[1], reverse=False)
    def num_edges(self):
        return self._graph.number_of_edges()

    def num_nodi(self):
        return len(self._artists_list)



