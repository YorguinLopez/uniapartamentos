# MainView.
# Creador: Yoruguin Lopez
# Creado: 2023-04-26
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-27
class MainView:
    def mostrar_menu(self):
        print("Bienvenido al sistema de registro de visitas\n")
        print("1. Registrar visita")
        print("2. Salir\n")

    def solicitar_datos_visita(self):
        num_piso = int(input("Ingrese el número de piso: "))
        num_apto = int(input("Ingrese el número de apartamento: "))
        nombre = input("Ingrese el nombre del visitante: ")
        cedula = input("Ingrese la cédula del visitante: ")
        return num_piso, num_apto, nombre, cedula

    def mostrar_confirmacion(self):
        print("Visita registrada correctamente\n")

    def mostrar_error(self, mensaje):
        print(mensaje)

    def iniciar(self, controlador):
        opcion = None
        while opcion != "2":
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                num_piso, num_apto, nombre, cedula = self.solicitar_datos_visita()
                controlador.registrar_visita(num_piso, num_apto, nombre, cedula)
                self.mostrar_confirmacion()
            elif opcion != "2":
                self.mostrar_error("Opción inválida")
        print("Adiós!")
