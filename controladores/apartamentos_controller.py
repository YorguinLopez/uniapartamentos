# ApartamentosController
# Creador: Yoruguin Lopez
# Creado: 2023-04-25
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-29

from modelos.apartamento import Apartamento
import json

class ApartamentosController:
    def __init__(self):
        self.apartamentos = []
        self.load_apartamentos()

    def load_apartamentos(self):
        try:
            with open('aptos.json', 'r') as f:
                aptos = json.load(f)
                for apto in aptos:
                    self.apartamentos.append(Apartamento(apto['num_piso'], apto['num_apto']))
        except FileNotFoundError:
            pass

    def get_apartamento(self, num_piso, num_apto):
        for apto in self.apartamentos:
            if apto.num_piso == num_piso and apto.num_apto == num_apto:
                return apto
        return None

    def agregar_visita(self, num_piso, num_apto, visita):
        apto = self.get_apartamento(num_piso, num_apto)
        if apto is None:
            apto = Apartamento(num_piso, num_apto)
            self.apartamentos.append(apto)
        apto.agregar_visita(visita)
        self.save_apartamentos()

    def toJSON(self):
        return [apto.toJSON() for apto in self.apartamentos]

    def save_apartamentos(self):
        with open('aptos.json', 'w') as f:
            json.dump(self.toJSON(), f)

