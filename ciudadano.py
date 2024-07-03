from enfermedad import Enfermedad

class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad, enfermedad=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__estado = True if enfermedad is None else False
        self.__dias_enfermo = 0

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellido(self, apellido):
        if isinstance(apellido, str):
            self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_comunidad(self, comunidad):
        if isinstance(comunidad, str):
            self.__comunidad = comunidad

    def get_comunidad(self):
        return self.__comunidad

    def set_enfermedad(self, enfermedad):
        if isinstance(enfermedad, Enfermedad):
            self.__enfermedad = enfermedad
            self.__estado = False
            self.__dias_enfermo = 0

    def get_enfermedad(self):
        return self.__enfermedad

    def set_estado(self, estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    def get_enfermo(self):
        return not self.__estado
        
    def set_enfermo(self, estado):
        self.__estado = not estado
        if estado:
            if self.__enfermedad is None:
                self.__enfermedad = Enfermedad(infeccion_probable=0.1, promedio_pasos=5)
            self.__dias_enfermo += 1
        else:
            self.__enfermedad = None
            self.__dias_enfermo = 0

    def get_dias_enfermo(self):
        return self.__dias_enfermo

    def __str__(self):
        return f"Ciudadano(id={self.__id}, nombre={self.__nombre}, apellido={self.__apellido}, enfermo={self.get_enfermo()}, dias_enfermo={self.__dias_enfermo})"

    def incrementar_dias_enfermo(self):
        if self.get_enfermo():
            self.__dias_enfermo += 1