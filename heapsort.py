def heap_sort(arr):
    lista = arr.copy()
    n = len(lista)

    def amontonar(sublista, tam, i):
        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < tam and sublista[izq] > sublista[mayor]:
            mayor = izq
        if der < tam and sublista[der] > sublista[mayor]:
            mayor = der

        if mayor != i:
            sublista[i], sublista[mayor] = sublista[mayor], sublista[i]
            amontonar(sublista, tam, mayor)

    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        amontonar(lista, n, i)

    # Extraer elementos uno por uno del montículo
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        amontonar(lista, i, 0)

    return lista

if __name__ == "__main__":
    datos = [12, 11, 13, 5, 6, 7]
    print("HeapSort - Original:", datos)
    print("HeapSort - Ordenado:", heap_sort(datos))
