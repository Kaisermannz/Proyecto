import csv
import random
import pandas as pd
import os


class Simulador:
    def __init__(self, comunidad, output_dir="resultados"):
        self.__comunidad = comunidad
        self.__dias_simulados = 0
        self.__total_infectados = 0
        self.__total_recuperados = 0
        self.__historial = []
        self.__output_dir = output_dir
        if not os.path.exists(self.__output_dir):
            os.makedirs(self.__output_dir)

    # Getters y Setters (los mantenemos como estaban)

    def ejecutar_simulacion(self, dias):
        for dia in range(dias):
            self.__simular_dia()
            self.__dias_simulados += 1
            self.__generar_informe()
            self.__exportar_a_csv()

    def __simular_dia(self):
        nuevos_infectados = 0
        nuevos_recuperados = 0
        for ciudadano in self.__comunidad.get_ciudadanos():
            if ciudadano.get_enfermo():
                nuevos_infectados += self.__propagar_enfermedad(ciudadano)
            estado_anterior = ciudadano.get_enfermo()
            self.__actualizar_estado(ciudadano)
            if estado_anterior and not ciudadano.get_enfermo():
                nuevos_recuperados += 1

        self.__total_infectados += nuevos_infectados
        self.__total_recuperados += nuevos_recuperados

    def __propagar_enfermedad(self, ciudadano_enfermo):
        nuevos_infectados = 0
        contactos = self.__obtener_contactos(ciudadano_enfermo)
        for contacto in contactos:
            if (
                not contacto.get_enfermo()
                and random.random()
                < self.__comunidad.get_enfermedad().get_infeccion_probable()
            ):
                contacto.set_enfermo(True)
                nueva_enfermedad = Enfermedad(
                    infeccion_probable=self.__comunidad.get_enfermedad().get_infeccion_probable(),
                    promedio_pasos=self.__comunidad.get_enfermedad().get_promedio_pasos(),
                )
                contacto.set_enfermedad(nueva_enfermedad)
                nueva_enfermedad.set_contador(0)
                nuevos_infectados += 1
        return nuevos_infectados

    def __actualizar_estado(self, ciudadano):
        if ciudadano.get_enfermo():
            enfermedad = ciudadano.get_enfermedad()
            if enfermedad is not None:
                enfermedad.set_contador(enfermedad.get_contador() + 1)
                if enfermedad.get_contador() >= enfermedad.get_promedio_pasos():
                    ciudadano.set_enfermo(False)
            else:
                print(
                    f"Advertencia: El ciudadano {ciudadano.get_id()} está enfermo pero no tiene una enfermedad asociada."
                )

    def __obtener_contactos(self, ciudadano):
        # Implementa la lógica para obtener los contactos de un ciudadano
        # Esto dependerá de cómo hayas implementado las conexiones en tu modelo
        return []  # Retorna una lista vacía por ahora

    def __generar_informe(self):
        infectados_activos = sum(
            1 for c in self.__comunidad.get_ciudadanos() if c.get_enfermo()
        )
        informe = {
            "dia": self.__dias_simulados,
            "infectados_activos": infectados_activos,
            "total_infectados": self.__total_infectados,
            "total_recuperados": self.__total_recuperados,
        }
        self.__historial.append(informe)
        print(
            f"Día {self.__dias_simulados}: Infectados activos: {infectados_activos}, "
            f"Total infectados: {self.__total_infectados}, Recuperados: {self.__total_recuperados}"
        )

    def __exportar_a_csv(self):
        nombre_archivo = os.path.join(
            self.__output_dir, f"simulacion_dia_{self.__dias_simulados}.csv"
        )
        datos = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            datos.append(
                {
                    "id": ciudadano.get_id(),
                    "nombre": ciudadano.get_nombre(),
                    "apellido": ciudadano.get_apellido(),
                    "enfermo": ciudadano.get_enfermo(),
                    "dias_enfermo": ciudadano.get_enfermedad().get_contador()
                    if ciudadano.get_enfermo()
                    else 0,
                }
            )

        df = pd.DataFrame(datos)
        df.to_csv(nombre_archivo, index=False)
        print(f"Datos exportados a {nombre_archivo}")

    def obtener_estadisticas(self):
        return {
            "dias_simulados": self.__dias_simulados,
            "total_infectados": self.__total_infectados,
            "total_recuperados": self.__total_recuperados,
            "historial": self.__historial,
        }
