# Modelo apartamento.
# Creador: Yoruguin Lopez
# Creado: 2023-04-26
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-27
from .visita import Visita

class Apartamento:
    # definimos propiedades del apartamento
    def __init__(self, num_piso, num_apto):
        self.num_piso = num_piso
        self.num_apto = num_apto
        self.visitas = []
    # Se agregan métodos para agregar visita
    def agregar_visita(self, visita):
        self.visitas.append(visita)

    def toJSON(self):
        return {"num_piso": self.num_piso, "num_apto": self.num_apto, "visitas": [visita.toJSON() for visita in self.visitas]}
