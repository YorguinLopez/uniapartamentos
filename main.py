# main.py
from controladores.apartamentos_controller import ApartamentosController
from controladores.visitas_controller import VisitasController
from modelos.apartamento import Apartamento
from modelos.visita import Visita
from utils.archivo import Archivo
from vistas.main_view import MainView

# Se crean las instancias necesarias
archivo_aptos = Archivo("data/aptos.json")
archivo_visitas = Archivo("data/visitas.json")
apartamentos = [Apartamento(piso, num_apto) for piso in range(1, 11) for num_apto in range(1, 5)]
visitas_controller = VisitasController(archivo_visitas, apartamentos)
apartamentos_controller = ApartamentosController(archivo_aptos, apartamentos)
main_view = MainView()

# Se inicia la vista principal
main_view.iniciar(visitas_controller, apartamentos_controller)
