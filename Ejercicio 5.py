def romano_a_decimal(romano):
    # Diccionario con los valores de cada símbolo romano
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Caso base: cadena vacía
    if not romano:
        return 0
    
    # Caso base: un solo carácter
    if len(romano) == 1:
        return valores[romano[0]]
    
    # Si el valor del primer carácter es mayor o igual al segundo
    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        # Si es menor, se resta el valor del primero al segundo
        return -valores[romano[0]] + romano_a_decimal(romano[1:])
    
print(romano_a_decimal("II"))