from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador
from generar_datos import generar_nombres, cargar_ciudadanos


def main():
    num_ciudadanos = 10000
    num_infectados_iniciales = 3
    generar_nombres(num_ciudadanos)
    
    # Parámetros del modelo SIR
    beta = 0.3  # Tasa de infección
    gamma = 1/20  # Tasa de recuperación (inverso del promedio de días de enfermedad)

    covid = Enfermedad(infeccion_probable=beta, promedio_pasos=14)
    talca = Comunidad(
        num_ciudadanos=num_ciudadanos,
        promedio_conexion_fisica=5,
        enfermedad=covid,
        num_infectados=num_infectados_iniciales,  # Comenzamos con 10 infectados
        probabilidad_conexion_fisica=0.3,
    )

    # Cargar ciudadanos desde el archivo CSV y agregarlos a la comunidad
    cargar_ciudadanos(talca, num_ciudadanos, num_infectados_iniciales, covid)

    # Crear una instancia de Simulador con los parámetros del modelo SIR
    simulador = Simulador(talca, beta=beta, gamma=gamma)

    # Simulación por 30 días
    dias_simulacion = 150
    simulador.ejecutar_simulacion(dias_simulacion)

    estadisticas = simulador.obtener_estadisticas()
    print("\nEstadísticas finales:")
    print(f"Días simulados: {estadisticas['dias_simulados']}")
    # Imprimir el último estado del modelo SIR
    ultimo_dia = estadisticas['historial'][-1]
    print(f"\nÚltimo día (día {ultimo_dia['dia']}):")
    print(f"Susceptibles: {ultimo_dia['susceptibles']}")
    print(f"Infectados: {ultimo_dia['infectados']}")
    print(f"Recuperados: {ultimo_dia['recuperados']}")

if __name__ == "__main__":
    main()