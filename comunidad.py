class Comunidad:
    def __init__(
        self,
        num_ciudadanos,
        promedio_conexion_fisica,
        enfermedad,
        num_infectados,
        probabilidad_conexion_fisica,
    ):
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.num_infectados = num_infectados
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.ciudadanos = []

    def agregar_ciudadano(self, ciudadano):
        self.ciudadanos.append(ciudadano)
