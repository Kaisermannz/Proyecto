from comunidad import Comunidad
from ciudadano import Ciudadano
from enfermedad import Enfermedad
import csv
from Ventana import create_simulacion_covid_app
from generar_datos import cargar_ciudadanos, generar_nombres


def main():
    # Configuración de la simulación
    num_ciudadanos = 10000
    num_infectados_iniciales = 2
    dias_simulacion = 75
    # Generar los nombres de las personas aleatoriamente
    generar_nombres(num_ciudadanos)

    # Crear la enfermedad
    covid19 = Enfermedad("COVID-19", probabilidad_contagio=0.07, duracion=4)

    # Crear la comunidad
    comunidad = Comunidad()

    # Cargar ciudadanos desde el archivo CSV
    ciudadanos = cargar_ciudadanos("datos/ciudadanos.csv", num_ciudadanos, comunidad)

    # Agregar ciudadanos a la comunidad
    for ciudadano in ciudadanos:
        comunidad.agregar_ciudadano(ciudadano)

    # Crear grupos en la comunidad
    comunidad.crear_grupos(promedio_grupos_por_persona=2, min_personas_por_grupo=3, max_personas_por_grupo=4)

    # Infectar aleatoriamente a algunos ciudadanos
    comunidad.infectar_aleatoriamente(num_infectados_iniciales, covid19)

    print("Estado inicial:")
    comunidad.imprimir_estadisticas()

    # Simular el contagio durante varios días
    for dia in range(1, dias_simulacion + 1):
        comunidad.simular_contagio_dias()
        print(f"\nDía {dia}:")
        comunidad.imprimir_estadisticas()

    print("\nGrupos formados:")
    comunidad.imprimir_grupos()

    comunidad.generar_grafica()

if __name__ == "__main__":
    main()
    app = create_simulacion_covid_app()
    app.run(None)
