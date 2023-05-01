# Modelo apartamento.
# Creador: Yoruguin Lopez
# Creado: 2023-04-26
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-27

class Visita:
    # Propiedades de la visita
    def __init__(self, nombre, cedula, fecha_hora):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_hora = fecha_hora
        self.apartamento = None

    # Métodos para administrar eventos
    def asociar_apartamento(self, apartamento):
        self.apartamento = apartamento
        apartamento.agregar_visita(self)

    def toJSON(self):
        return {"nombre": self.nombre, "cedula": self.cedula, "fecha_hora": self.fecha_hora, "apartamento": self.apartamento.toJSON()}
