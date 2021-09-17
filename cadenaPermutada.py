from itertools import permutations


def permutar(n):
    if (0 < n < 10 and type(n) == int):
        cadenaPermutada = ''
        arregloAPermutar = []
        for i in range(n):
            arregloAPermutar.append(str(i + 1))

        arregloPermutado = permutations(arregloAPermutar)
        for permutacion in arregloPermutado:
            cadenaPermutada += ''.join(permutacion) + ', '

        return cadenaPermutada[:-2]
    else:
        return 'El número ingresado debe ser entero, mayor que 0 y menor que 10'


if __name__ == '__main__':
    print(permutar(4))
