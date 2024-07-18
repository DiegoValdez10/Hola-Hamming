def calcular_paridad(bits, posiciones):
    paridad = 0
    for pos in posiciones:
        if bits[pos-1] is not None:
            paridad ^= bits[pos-1]
    return paridad

def corregir_y_decodificar(bloque):
    posiciones_paridad = {
        1: [1, 3, 5, 7, 9, 11],
        2: [2, 3, 6, 7, 10, 11],
        3: [4, 5, 6, 7],
        4: [8, 9, 10, 11]
    }
    
    codigo_hamming = [int(bit) for bit in bloque]
    
    sindrome = 0
    for p in posiciones_paridad:
        if calcular_paridad(codigo_hamming, posiciones_paridad[p]) != 0:
            sindrome += p
    
    if sindrome != 0:
        codigo_hamming[sindrome-1] ^= 1
    
    posiciones_datos = [3, 5, 6, 7, 9, 10, 11]
    bits_datos = [codigo_hamming[pos-1] for pos in posiciones_datos]
    
    return bits_datos

def codificar_hamming_11_7(bits_datos):
    codigo_hamming = [0] * 11
    
    posiciones_datos = [2, 4, 5, 6, 8, 9, 10]
    for i, pos in enumerate(posiciones_datos):
        codigo_hamming[pos] = int(bits_datos[i])
    
    posiciones_paridad = {
        0: [1, 3, 5, 7, 9, 11],
        1: [2, 3, 6, 7, 10, 11],
        3: [4, 5, 6, 7],
        7: [8, 9, 10, 11]
    }
    
    for p in posiciones_paridad:
        valor_paridad = calcular_paridad(codigo_hamming, posiciones_paridad[p])
        codigo_hamming[p] = valor_paridad
    
    return ''.join(map(str, codigo_hamming))

def introducir_error(bits_codificados, posicion):
    bits_codificados = list(bits_codificados)
    bits_codificados[posicion] = '1' if bits_codificados[posicion] == '0' else '0'
    return ''.join(bits_codificados)

ascii_A = 65
binario_A = format(ascii_A, '07b')
print(f'Binario de "A": {binario_A}')

hamming_codificado_A = codificar_hamming_11_7(binario_A)
print(f'Hamming codificado de "A": {hamming_codificado_A}')

hamming_codificado_A_con_error = introducir_error(hamming_codificado_A, 4)
print(f'Hamming codificado de "A" con error: {hamming_codificado_A_con_error}')

bits_corregidos = corregir_y_decodificar(hamming_codificado_A_con_error)
print(f'Bits corregidos de "A": {bits_corregidos}')

binario_A_corregido = ''.join(map(str, bits_corregidos))
print(f'Bits originales de "A": {binario_A}')
print(f'Bits corregidos coinciden con originales: {binario_A_corregido == binario_A}')