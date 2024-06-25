from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador
from generar_datos import generar_nombres, cargar_ciudadanos


def main():
    generar_nombres()

    covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=14)

    talca = Comunidad(
        num_ciudadanos=1000,
        promedio_conexion_fisica=5,
        enfermedad=covid,
        num_infectados=10,
        probabilidad_conexion_fisica=0.3,
    )

    # cargar ciudadanos desde el archivo CSV y agregarlos a la comunidad
    cargar_ciudadanos(talca)

    # Crear una instancia de Simulador
    simulador = Simulador(talca)

    # simulación por 30 días
    dias_simulacion = 30
    simulador.ejecutar_simulacion(dias_simulacion)

    estadisticas = simulador.obtener_estadisticas()
    print("\nEstadísticas finales:")
    print(f"Días simulados: {estadisticas['dias_simulados']}")
    print(f"Total de infectados: {estadisticas['total_infectados']}")
    print(f"Total de recuperados: {estadisticas['total_recuperados']}")


if __name__ == "__main__":
    main()
