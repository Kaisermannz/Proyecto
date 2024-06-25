class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos):
        self.__infeccion_probable = infeccion_probable
        self.__promedio_pasos = promedio_pasos
        self.__enfermo = False
        self.__contador = 0

    # Getters
    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def get_promedio_pasos(self):
        return self.__promedio_pasos

    def get_enfermo(self):
        return self.__enfermo

    def get_contador(self):
        return self.__contador

    # Setters
    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable = infeccion_probable

    def set_promedio_pasos(self, promedio_pasos):
        self.__promedio_pasos = promedio_pasos

    def set_enfermo(self, enfermo):
        self.__enfermo = enfermo

    def set_contador(self, contador):
        self.__contador = contador
