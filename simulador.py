import csv
import random
import pandas as pd
import os
import numpy as np

class Simulador:
    def __init__(self, comunidad, output_dir="resultados", beta=0.3, gamma=0.071):
        self.__comunidad = comunidad
        self.__dias_simulados = 0
        self.__output_dir = output_dir
        if not os.path.exists(self.__output_dir):
            os.makedirs(self.__output_dir)
        
        # Atributos modelo SIR
        self.__N = len(comunidad.get_ciudadanos())  # Población total
        self.__beta = beta  # Tasa de infección
        self.__gamma = gamma  # Tasa de recuperación
        self.__dt = 1  # Paso de tiempo 1 día

        # Creamos valores como arrays de NumPy
        self.__S = np.array(self.__N - comunidad.get_num_infectados(), dtype=float)
        self.__I = np.array(comunidad.get_num_infectados(), dtype=float)
        self.__R = np.array(0, dtype=float)
        self.__total_infectados = np.array(comunidad.get_num_infectados(), dtype=float)
        self.__total_recuperados = np.array(0, dtype=float)

        self.__historial = []

    def ejecutar_simulacion(self, dias):
        for dia in range(dias):
            self.__simular_dia()
            self.__dias_simulados += 1
            self.__generar_informe()
            self.__exportar_a_csv()

    def __simular_dia(self):
        
        dSdt = -self.__beta * self.__S * self.__I / self.__N
        dIdt = self.__beta * self.__S * self.__I / self.__N - self.__gamma * self.__I
        dRdt = self.__gamma * self.__I

        
        new_S = self.__S + dSdt * self.__dt
        new_I = self.__I + dIdt * self.__dt
        new_R = self.__R + dRdt * self.__dt

        
        new_S = np.maximum(0, new_S)
        new_I = np.maximum(0, new_I)
        new_R = np.maximum(0, new_R)

        #  suma es igual a N
        total = new_S + new_I + new_R
        if total != self.__N:
            factor = self.__N / total
            new_S *= factor
            new_I *= factor
            new_R *= factor

        # Calculamos los cambios reales
        delta_S = new_S - self.__S
        delta_I = new_I - self.__I
        delta_R = new_R - self.__R

        # Actualizamos los valores
        self.__S = new_S
        self.__I = new_I
        self.__R = new_R

        # Actualizamos los contadores globales
        self.__total_infectados += np.maximum(0, delta_I)
        self.__total_recuperados += np.maximum(0, delta_R)

        # Actualizamos el estado de los ciudadanos
        ciudadanos = self.__comunidad.get_ciudadanos()
        num_infectados = int(np.round(self.__I))
        estados = np.zeros(self.__N, dtype=bool)
        estados[:num_infectados] = True
        np.random.shuffle(estados)
        for ciudadano, estado in zip(ciudadanos, estados):
            ciudadano.set_enfermo(estado)
            if estado:
                ciudadano.incrementar_dias_enfermo()

    def __generar_informe(self):
        informe = {
            "dia": self.__dias_simulados,
            "susceptibles": int(np.round(self.__S)),
            "infectados": int(np.round(self.__I)),
            "recuperados": int(np.round(self.__R)),
            "total_infectados": int(np.round(self.__total_infectados)),
            "total_recuperados": int(np.round(self.__total_recuperados)),
        }
        self.__historial.append(informe)
        print(
            f"Día {self.__dias_simulados}: Susceptibles: {informe['susceptibles']}, "
            f"Infectados: {informe['infectados']}, Recuperados: {informe['recuperados']}, "
        )

    def __exportar_a_csv(self):
        nombre_archivo = os.path.join(
            self.__output_dir, f"simulacion_dia_{self.__dias_simulados}.csv")
        datos = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            dato = {
                "id": ciudadano.get_id(),
                "nombre": ciudadano.get_nombre(),
                "apellido": ciudadano.get_apellido(),
                "enfermo": ciudadano.get_enfermo(),
                "dias_enfermo": ciudadano.get_dias_enfermo() if ciudadano.get_enfermo() else 0,
            }
            datos.append(dato)
            
        df = pd.DataFrame(datos)
        
        df.to_csv(nombre_archivo, index=False)

    def obtener_estadisticas(self):
        return {
            "dias_simulados": self.__dias_simulados,
            "historial": self.__historial,
        }