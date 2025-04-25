def usar_la_fuerza(mochila, objetos_sacados=0):
 
    if not mochila:
        return (False, objetos_sacados)
    
  
    objeto = mochila.pop(0)
    objetos_sacados += 1
    
    print(f"El Jedi saca un {objeto}...")
    
   
    if objeto == "sable de luz":
        print("¡El Jedi encontró el sable de luz!")
        return (True, objetos_sacados)
    
   
    return usar_la_fuerza(mochila, objetos_sacados)


mochila_rey = ["comida", "mapa", "brújula", "sable de luz", "ropa", "kit médico"]
encontrado, cantidad = usar_la_fuerza(mochila_rey.copy())  

print(f"\nResultado:")
print(f"¿Encontró el sable de luz?: {'Sí' if encontrado else 'No'}")
print(f"Objetos sacados: {cantidad}")


mochila_obiwan = ["comida", "mapa", "brújula", "ropa", "kit médico"]
print("\nPrueba sin sable de luz:")
encontrado, cantidad = usar_la_fuerza(mochila_obiwan.copy())
print(f"\nResultado:")
print(f"¿Encontró el sable de luz?: {'Sí' if encontrado else 'No'}")
print(f"Objetos sacados: {cantidad}")