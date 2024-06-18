class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad, enfermedad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.comunidad = comunidad
        self.enfermedad = enfermedad
        self.estado = True  # True para sano, False para enfermo/muerto
