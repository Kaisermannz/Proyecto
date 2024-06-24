from enfermedad import Enfermedad


class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad, enfermedad=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__estado = (
            False if enfermedad else True
        )  # True para sano False para enfermo/muerto

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
        if isinstance(apellido, int):
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
        if estado and self.__enfermedad is None:
            self.__enfermedad = Enfermedad(
                infeccion_probable=0.1, promedio_pasos=5
            )  # Ejemplo de valores
        elif not estado:
            self.__enfermedad = None

