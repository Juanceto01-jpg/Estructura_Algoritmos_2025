def usar_la_fuerza(mochila, objetos_sacados=0):
 
    if not mochila:
        return (False, objetos_sacados)
    
    objeto = mochila.pop(0)
    objetos_sacados += 1
    
    if objeto == "Sable_de_luz":
        print("¡El Jedi encontró el sable de luz!")
        return (True, objetos_sacados)
    
   
    return usar_la_fuerza(mochila, objetos_sacados)


saco_de_luke = ["Comida", "Agua", "Sable_de_luz"]
encontrado, cantidad = usar_la_fuerza(saco_de_luke.copy())

print(f"¿encontro el sable de luz?: {"si" if encontrado else "no" }")
print(f"Objetos sacados para encontrar el sable: {cantidad}")
