import csv
from ciudadano import Ciudadano
import random

def generar_nombres(num):
    nombres = [
        "Juan",
        "Maria",
        "Luis",
        "Ana",
        "Hugo",
        "Mateo",
        "Martín",
        "Lucas",
        "Leo",
        "Daniel",
        "Alejandro",
        "Manuel",
        "Pablo",
        "Álvaro",
        "Adrián",
        "Enzo",
        "Mario",
        "Diego",
        "David",
        "Oliver",
        "Marcos",
        "Thiago",
        "Marco",
        "Álex",
        "Javier",
        "Izan",
        "Bruno",
        "Miguel",
        "Antonio",
        "Gonzalo",
        "Liam",
        "Gael",
        "Marc",
        "Carlos",
        "Juan",
        "Ángel",
        "Dylan",
        "Nicolás",
        "José",
        "Sergio",
        "Gabriel",
        "Luca",
        "Jorge",
        "Darío",
        "Íker",
        "Samuel",
        "Eric",
        "Adam",
        "Héctor",
        "Francisco",
        "Rodrigo",
        "Jesús",
        "Erik",
        "Amir",
        "Jaime",
        "Ian",
        "Rubén",
        "Aarón",
        "Iván",
        "Pau",
        "Víctor",
        "Guillermo",
        "Luis",
        "Mohamed",
        "Pedro",
        "Julen",
        "Unai",
        "Rafael",
        "Santiago",
        "Saúl",
        "Alberto",
        "Noah",
        "Aitor",
        "Joel",
        "Nil",
        "Jan",
        "Pol",
        "Raúl",
        "Matías",
        "Martí",
        "Fernando",
        "Andrés",
        "Rayan",
        "Alonso",
        "Ismael",
        "Asier",
        "Biel",
        "Ander",
        "Aleix",
        "Axel",
        "Alan",
        "Ignacio",
        "Fabio",
        "Neizan",
        "Jon",
        "Teo",
        "Isaac",
        "Arnau",
        "Luka",
        "Max",
        "Imran",
        "Youssef",
        "Anas",
        "Elías",
    ]
    apellidos = [
        "Perez",
        "Gomez",
        "Rodriguez",
        "Fernandez",
        "Abaigar",
        "Adei",
        "Adur",
        "Adiran",
        "Aimar",
        "Aitor",
        "Andoni",
        "Ander",
        "Antxon",
        "Amets",
        "Aratz",
        "Argi",
        "Aritz",
        "Asier",
        "Balkoe",
        "Baltz",
        "Bazkoare",
        "Beltso",
        "Bernat",
        "Beñat",
        "Bikendi",
        "Biktor",
        "Bizen",
        "Dabi",
        "Dari",
        "Damen",
        "Diagur",
        "Dunixi",
        "Eako",
        "Eder",
        "Edorta",
        "Edur",
        "Eki",
        "Ekaitz",
        "Eladi",
        "Elixi",
        "Eloi",
        "Emiri",
        "Eneko",
        "Endrike",
        "Eritz",
        "Etor",
        "Euken",
        "Ferran",
        "Frantzisko",
        "Ganiz",
        "Gari",
        "Gentzen",
        "Gergori",
        "Gilem",
        "Gizon",
        "Goiznabar",
        "Gontzal",
        "Gorka",
        "Grazian",
        "Guren",
        "Haize",
        "Haran",
        "Haritz",
        "Heiko",
        "Hodei",
        "Ibai",
        "Ibar",
        "Igon",
        "Igor",
        "Iker",
        "Imanol",
        "Iñaki",
        "Ipar",
        "Irai",
        "Iren",
        "Izan",
        "Izei",
        "Jon",
        "Jeino",
        "Joritz",
        "Josu",
        "Julen",
        "Jurgi",
        "Kai",
        "Kasi",
        "Kauldi",
        "Kutun",
        "Lain",
        "Luken",
        "Maide",
        "Mairu",
        "Maren",
        "Markel",
        "Martitz",
        "Mikel",
        "Negu",
        "Neketi",
        "Nikanor",
        "Odei",
        "Oier",
        "Oihan",
        "Orentzi",
        "Orixe",
        "Ortzadar",
        "Ostertz",
        "Paken",
        "Patxi",
        "Roke",
        "Sanduru",
        "Semenko",
        "Sendoa",
        "Silban",
        "Sukil",
        "Todor",
        "Txarles",
        "Ugutz",
        "Uhaitz",
        "Unai",
        "Untzalu",
        "Urtzi",
        "Uztai",
        "Xabier",
        "Zuhaitz",
        "Zuri",
        "Zuzen",
    ]

    with open("datos/ciudadanos.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "nombre", "apellido"])

        for i in range(num):
            writer.writerow(
                [i, nombres[i % len(nombres)], apellidos[i % len(apellidos)]]
            )


def cargar_ciudadanos(comunidad, num_ciudadanos, num_infectados, enfermedad):
    ciudadanos_cargados = 0
    infectados_iniciales = 0
    
    with open("datos/ciudadanos.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if ciudadanos_cargados >= num_ciudadanos:
                break
            
            esta_enfermo = infectados_iniciales < num_infectados and random.random() < 0.5
            
            ciudadano = Ciudadano(
                id=int(row["id"]),
                nombre=row["nombre"],
                apellido=row["apellido"],
                comunidad=comunidad,
                enfermedad=enfermedad if esta_enfermo else None
            )
            
            if esta_enfermo:
                ciudadano.set_enfermo(True)
                infectados_iniciales += 1
            
            comunidad.agregar_ciudadano(ciudadano)
            ciudadanos_cargados += 1
    
    # Si no hay suficientes ciudadanos en el CSV, creamos más
    while ciudadanos_cargados < num_ciudadanos:
        esta_enfermo = infectados_iniciales < num_infectados and random.random() < 0.5
        
        ciudadano = Ciudadano(
            id=ciudadanos_cargados + 1,
            nombre=f"Ciudadano{ciudadanos_cargados + 1}",
            apellido=f"Apellido{ciudadanos_cargados + 1}",
            comunidad=comunidad,
            enfermedad=enfermedad if esta_enfermo else None
        )
        
        if esta_enfermo:
            ciudadano.set_enfermo(True)
            infectados_iniciales += 1
        
        comunidad.agregar_ciudadano(ciudadano)
        ciudadanos_cargados += 1
    
    print(f"Se cargaron {ciudadanos_cargados} ciudadanos, de los cuales {infectados_iniciales} están inicialmente infectados.")