import csv
import random
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

class Simulador:
    def __init__(self, comunidad, output_dir, beta, gamma):
        self.__comunidad = comunidad
        self.__dias_simulados = 0
        self.__output_dir = output_dir
        if not os.path.exists(self.__output_dir):
            os.makedirs(self.__output_dir)
        
        # Parámetros del modelo SIR
        self.__N = len(comunidad.get_ciudadanos())  # Población total
        self.__beta = beta  # Tasa de infección
        self.__gamma = gamma  # Tasa de recuperación
        self.__dt = 1  # Paso de tiempo 1 día

        # Inicialización de los compartimentos SIR
        self.__S = self.__N - comunidad.get_num_infectados()  # Susceptibles iniciales
        self.__I = comunidad.get_num_infectados()  # Infectados iniciales
        self.__R = 0  # Recuperados iniciales

        self.__historial = []

    def ejecutar_simulacion(self, dias):
        for _ in range(dias):
            self.__simular_dia()
            self.__generar_informe()
            self.__exportar_a_csv()
        self.generar_grafica()

    def __simular_dia(self):
        ciudadanos = self.__comunidad.get_ciudadanos()
        
        # Calcular nuevos infectados y recuperados
        nuevos_infectados = np.random.binomial(self.__S, self.__beta * self.__I / self.__N)
        nuevos_recuperados = np.random.binomial(self.__I, self.__gamma)

        # Actualizar contadores
        self.__S -= nuevos_infectados
        self.__I += nuevos_infectados - nuevos_recuperados
        self.__R += nuevos_recuperados

        # Asegurarse de que los valores no sean negativos
        self.__S = max(0, self.__S)
        self.__I = max(0, self.__I)
        self.__R = max(0, self.__R)

        # Actualizar estado de los ciudadanos
        susceptibles = []
        for c in ciudadanos:
            if c.get_estado() == "susceptible":
                susceptibles.append(c)
            
        infectados = []
        for c in ciudadanos:
            if c.get_estado() == "infectado":
                infectados.append(c)

        # Infectar nuevos
        for ciudadano in random.sample(susceptibles, min(nuevos_infectados, len(susceptibles))):
            ciudadano.set_estado("infectado")

        # Recuperar
        for ciudadano in random.sample(infectados, min(nuevos_recuperados, len(infectados))):
            ciudadano.set_estado("recuperado")

        # Incrementar días de enfermedad para los infectados
        for ciudadano in ciudadanos:
            if ciudadano.get_estado() == "infectado":
                ciudadano.incrementar_dias_enfermo()

        self.__dias_simulados += 1

    def __generar_informe(self):
        informe = {
            "dia": self.__dias_simulados,
            "susceptibles": int(self.__S),
            "infectados": int(self.__I),
            "recuperados": int(self.__R),
        }
        self.__historial.append(informe)
        print(
            f"Día {self.__dias_simulados}: Susceptibles: {informe['susceptibles']}, "
            f"Infectados: {informe['infectados']}, Recuperados: {informe['recuperados']}"
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
                "estado": ciudadano.get_estado(),
                "dias_enfermo": ciudadano.get_dias_enfermo(),
            }
            datos.append(dato)
            
        df = pd.DataFrame(datos)
        df.to_csv(nombre_archivo, index=False)

    def obtener_estadisticas(self):
        return {
            "dias_simulados": self.__dias_simulados,
            "historial": self.__historial,
        }


    def generar_grafica(self):
        dias = [informe['dia'] for informe in self.__historial]
        susceptibles = [informe['susceptibles'] for informe in self.__historial]
        infectados = [informe['infectados'] for informe in self.__historial]
        recuperados = [informe['recuperados'] for informe in self.__historial]

        plt.figure(figsize=(10, 6))
        plt.plot(dias, susceptibles, label='Susceptibles', color='blue')
        plt.plot(dias, infectados, label='Infectados', color='red')
        plt.plot(dias, recuperados, label='Recuperados', color='green')

        plt.title('Modelo SIR - Evolución de la epidemia')
        plt.xlabel('Días')
        plt.ylabel('Número de individuos')
        plt.legend()
        plt.grid(True)

        # Guardar la gráfica
        plt.savefig(os.path.join(self.__output_dir, 'grafica_SIR.png'))
        plt.close()