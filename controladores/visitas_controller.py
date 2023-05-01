# VistasController.
# Creador: Yoruguin Lopez
# Creado: 2023-04-25
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-27
from modelos.apartamento import Apartamento
from modelos.visita import Visita
from utils.archivo import cargar_datos, guardar_datos
import datetime

class VisitasController:
    def __init__(self):
        self.apartamentos = self.cargar_apartamentos()
        self.visitas = self.cargar_visitas()

    def cargar_apartamentos(self):
        data = cargar_datos("aptos.json")
        apartamentos = []
        for piso in data:
            for apto in piso["apartamentos"]:
                apartamento = Apartamento(piso["num_piso"], apto["num_apto"])
                for visita in apto["visitas"]:
                    v = Visita(visita["nombre"], visita["cedula"], datetime.datetime.strptime(visita["fecha_hora"], "%Y-%m-%d %H:%M:%S.%f"))
                    apartamento.agregar_visita(v)
                apartamentos.append(apartamento)
        return apartamentos

    def cargar_visitas(self):
        data = cargar_datos("visitas.json")
        visitas = []
        for visita in data:
            v = Visita(visita["nombre"], visita["cedula"], datetime.datetime.strptime(visita["fecha_hora"], "%Y-%m-%d %H:%M:%S.%f"))
            apartamento = self.buscar_apartamento(visita["apartamento"]["num_piso"], visita["apartamento"]["num_apto"])
            if apartamento:
                v.asociar_apartamento(apartamento)
            visitas.append(v)
        return visitas

    def buscar_apartamento(self, num_piso, num_apto):
        for apto in self.apartamentos:
            if apto.num_piso == num_piso and apto.num_apto == num_apto:
                return apto
        return None

    def registrar_visita(self, num_piso, num_apto, nombre, cedula):
        apartamento = self.buscar_apartamento(num_piso, num_apto)
        if apartamento:
            visita = Visita(nombre, cedula, datetime.datetime.now())
            visita.asociar_apartamento(apartamento)
            self.visitas.append(visita)
            guardar_datos("visitas.json", [v.toJSON() for v in self.visitas])
            guardar_datos("aptos.json", [apto.toJSON() for apto in self.apartamentos])
        else:
            print("El apartamento no existe")
