from enfermedad import Enfermedad

class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad, enfermedad=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__estado = "susceptible"
        self.__dias_enfermo = 0

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_comunidad(self):
        return self.__comunidad

    def get_enfermedad(self):
        return self.__enfermedad

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        if estado in ["susceptible", "infectado", "recuperado"]:
            if estado == "infectado" and self.__estado == "susceptible":
                self.__estado = estado
            elif estado == "recuperado" and self.__estado == "infectado":
                self.__estado = estado
                self.__enfermedad = None
            elif estado == "susceptible" and self.__estado != "recuperado":
                self.__estado = estado
                self.__enfermedad = None
                self.__dias_enfermo = 0

    def get_enfermo(self):
        return self.__estado == "infectado"
        
    def set_enfermo(self, estado):
        if estado:
            self.set_estado("infectado")
        else:
            self.set_estado("recuperado")

    def get_dias_enfermo(self):
        return self.__dias_enfermo

    def incrementar_dias_enfermo(self):
        if self.__estado == "infectado":
            self.__dias_enfermo += 1

    def __str__(self):
        return f"Ciudadano(id={self.__id}, nombre={self.__nombre}, apellido={self.__apellido}, estado={self.__estado}, dias_enfermo={self.__dias_enfermo})"