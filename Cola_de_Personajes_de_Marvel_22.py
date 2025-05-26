from collections import deque


class Personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero.upper()  
    
    def __str__(self):
        return f"Personaje: {self.nombre_personaje} | Superhéroe: {self.nombre_superheroe} | Género: {self.genero}"


def cargar_personajes():
    cola = deque([
        Personaje("Tony Stark", "Iron Man", "M"),
        Personaje("Steve Rogers", "Capitán América", "M"),
        Personaje("Natasha Romanoff", "Black Widow", "F"),
        Personaje("Carol Danvers", "Capitana Marvel", "F"),
        Personaje("Scott Lang", "Ant-Man", "M"),
        Personaje("Peter Parker", "Spider-Man", "M"),
        Personaje("Stephen Strange", "Doctor Strange", "M"),
        Personaje("Wanda Maximoff", "Scarlet Witch", "F"),
        Personaje("Sam Wilson", "Falcon", "M"),
        Personaje("Shuri", "Black Panther", "F"),
        Personaje("Thor Odinson", "Thor", "M")
    ])
    return cola


def nombre_personaje_capitana_marvel(cola):
    cola_temporal = deque()
    nombre_personaje = None
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if personaje.nombre_superheroe.lower() == "capitana marvel":
            nombre_personaje = personaje.nombre_personaje
    
    
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return nombre_personaje


def superheroes_femeninos(cola):
    cola_temporal = deque()
    superheroinas = []
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if personaje.genero == "F":
            superheroinas.append(personaje.nombre_superheroe)
    
    
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return superheroinas


def personajes_masculinos(cola):
    cola_temporal = deque()
    masculinos = []
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if personaje.genero == "M":
            masculinos.append(personaje.nombre_personaje)
    
    
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return masculinos


def superheroe_scott_lang(cola):
    cola_temporal = deque()
    nombre_superheroe = None
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if personaje.nombre_personaje.lower() == "scott lang":
            nombre_superheroe = personaje.nombre_superheroe
    
   
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return nombre_superheroe


def personajes_comienzan_con_S(cola):
    cola_temporal = deque()
    resultados = []
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if (personaje.nombre_personaje.lower().startswith('s') or 
            personaje.nombre_superheroe.lower().startswith('s')):
            resultados.append(personaje)
    
  
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return resultados


def carol_danvers_info(cola):
    cola_temporal = deque()
    encontrado = False
    nombre_superheroe = None
    
    while cola:
        personaje = cola.popleft()
        cola_temporal.append(personaje)
        
        if personaje.nombre_personaje.lower() == "carol danvers":
            encontrado = True
            nombre_superheroe = personaje.nombre_superheroe
            break  
    
   
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return encontrado, nombre_superheroe


def mostrar_lista(elementos, titulo):
    print(f"\n--- {titulo} ---")
    for elemento in elementos:
        print(elemento)
    print()


if __name__ == "__main__":
    cola_mcu = cargar_personajes()
    
   
    nombre = nombre_personaje_capitana_marvel(cola_mcu.copy())
    print(f"a. El personaje de Capitana Marvel es: {nombre}")
    
    
    superheroinas = superheroes_femeninos(cola_mcu.copy())
    mostrar_lista(superheroinas, "b. Superhéroes femeninos")
    
    
    masculinos = personajes_masculinos(cola_mcu.copy())
    mostrar_lista(masculinos, "c. Personajes masculinos")
    
    
    superheroe = superheroe_scott_lang(cola_mcu.copy())
    print(f"d. El superhéroe de Scott Lang es: {superheroe}")
    
   
    personajes_S = personajes_comienzan_con_S(cola_mcu.copy())
    mostrar_lista(personajes_S, "e. Personajes/superhéroes que comienzan con S")
    
    
    encontrado, nombre_sh = carol_danvers_info(cola_mcu.copy())
    if encontrado:
        print(f"f. Carol Danvers está en la cola y su nombre de superhéroe es: {nombre_sh}")
    else:
        print("f. Carol Danvers no se encuentra en la cola")
