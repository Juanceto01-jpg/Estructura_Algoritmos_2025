from queue_ import Queue

class Personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero.upper()


def mostrar_personaje(p):
    print("Personaje:", p.nombre_personaje)
    print("Superhéroe:", p.nombre_superheroe)
    print("Género:", p.genero)


def cargar_personajes():
    cola = Queue()
    datos = [
        ("Tony Stark", "Iron Man", "M"),
        ("Steve Rogers", "Capitán América", "M"),
        ("Natasha Romanoff", "Black Widow", "F"),
        ("Carol Danvers", "Capitana Marvel", "F"),
        ("Scott Lang", "Ant-Man", "M"),
        ("Peter Parker", "Spider-Man", "M"),
        ("Stephen Strange", "Doctor Strange", "M"),
        ("Wanda Maximoff", "Scarlet Witch", "F"),
        ("Sam Wilson", "Falcon", "M"),
        ("Shuri", "Black Panther", "F"),
        ("Thor Odinson", "Thor", "M")
    ]
    for i in range(len(datos)):
        nombre, heroe, genero = datos[i]
        cola.arrive(Personaje(nombre, heroe, genero))
    return cola


def nombre_personaje_capitana_marvel(cola):
    aux = Queue()
    resultado = None
    while not cola.is_empty():
        p = cola.attention()
        if p.nombre_superheroe.lower() == "capitana marvel":
            resultado = p.nombre_personaje
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return resultado


def superheroes_femeninos(cola):
    aux = Queue()
    resultados = []
    while not cola.is_empty():
        p = cola.attention()
        if p.genero == "F":
            resultados.append(p.nombre_superheroe)
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return resultados


def personajes_masculinos(cola):
    aux = Queue()
    resultados = []
    while not cola.is_empty():
        p = cola.attention()
        if p.genero == "M":
            resultados.append(p.nombre_personaje)
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return resultados


def superheroe_scott_lang(cola):
    aux = Queue()
    resultado = None
    while not cola.is_empty():
        p = cola.attention()
        if p.nombre_personaje.lower() == "scott lang":
            resultado = p.nombre_superheroe
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return resultado


def personajes_comienzan_con_S(cola):
    aux = Queue()
    resultados = []
    while not cola.is_empty():
        p = cola.attention()
        nombre = p.nombre_personaje.lower()
        heroe = p.nombre_superheroe.lower()
        if nombre.startswith("s") or heroe.startswith("s"):
            resultados.append(p)
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return resultados


def carol_danvers_info(cola):
    aux = Queue()
    encontrado = False
    superheroe = None
    while not cola.is_empty():
        p = cola.attention()
        if not encontrado and p.nombre_personaje.lower() == "carol danvers":
            superheroe = p.nombre_superheroe
            encontrado = True
        aux.arrive(p)
    while not aux.is_empty():
        cola.arrive(aux.attention())
    return encontrado, superheroe


def mostrar_lista(lista, titulo):
    print(titulo)
    for i in range(len(lista)):
        if isinstance(lista[i], Personaje):
            mostrar_personaje(lista[i])
        else:
            print(lista[i])
    print()


if __name__ == "__main__":
    cola_mcu = cargar_personajes()

    nombre = nombre_personaje_capitana_marvel(cola_mcu)
    print("a) El personaje de Capitana Marvel es:", nombre)

    mostrar_lista(superheroes_femeninos(cola_mcu), "b) Superhéroes femeninos:")

    mostrar_lista(personajes_masculinos(cola_mcu), "c) Personajes masculinos:")

    print("d) Superhéroe de Scott Lang:", superheroe_scott_lang(cola_mcu))

    mostrar_lista(personajes_comienzan_con_S(cola_mcu), "e) Personajes o superhéroes que comienzan con 'S':")

    encontrado, sh = carol_danvers_info(cola_mcu)
    if encontrado:
        print("f) Carol Danvers está en la cola y su superhéroe es:", sh)
    else:
        print("f) Carol Danvers no se encuentra en la cola.")

