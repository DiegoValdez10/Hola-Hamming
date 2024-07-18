def calcular_paridad(bits, posiciones):
    paridad = 0
    for pos in posiciones:
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

bloques = [
    "10110010000",
    "10110011111",
    "10110011100",
    "10100001001",
    "10011000000",
    "01010010101",
    "01100100101",
    "01110010110",
    "01100000100",
    "10110011111"
]

bits_mensaje_decodificado = []
for bloque in bloques:
    bits_mensaje_decodificado.extend(corregir_y_decodificar(bloque))

caracteres_ascii = []
for i in range(0, len(bits_mensaje_decodificado), 7):
    bits_caracter = bits_mensaje_decodificado[i:i+7]
    valor_caracter = int(''.join(map(str, bits_caracter)), 2)
    caracteres_ascii.append(chr(valor_caracter))

mensaje_decodificado = ''.join(caracteres_ascii)
print(f"Mensaje decodificado: {mensaje_decodificado}")