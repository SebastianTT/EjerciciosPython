if __name__ == '__main__':
    trama = ['58A6', 'FC89', 'BD1A', '4313', '1250', '0F21', 'C89B', 'D1A4']
    for i in trama:
        hexadecimalAEntero = int(i, base=16)
        binario = bin(hexadecimalAEntero)[2:].zfill(16)
        print(f'HEXADECIMAL: {i}')
        print(f"ESTADO: {'Encendido' if binario[0] == '1' else 'Apagado'}")
        print(f'LEDS EN TOTAL: {int(binario[1:8], 2)}')
        print(f'VALOR DEL PULSO {int(binario[8::], 2)}')
        print('\n')
