from random import randint


def ordenar_arreglo(arregloDesordenado):
    return sorted(arregloDesordenado)


if __name__ == '__main__':
    arregloDesordenado = []
    for i in range(20):
        arregloDesordenado.append(randint(0, 1000))
    print(f'Arreglo desordenado: {arregloDesordenado}')
    print(f'Arreglo ordenado: {ordenar_arreglo(arregloDesordenado)}')
