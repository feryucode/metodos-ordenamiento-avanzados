def quick_sort(arr):
    lista = arr.copy()
    
    def _quicksort(sublista, bajo, alto):
        if bajo < alto:
            pivote_idx = particion(sublista, bajo, alto)
            _quicksort(sublista, bajo, pivote_idx - 1)
            _quicksort(sublista, pivote_idx + 1, alto)

    def particion(sublista, bajo, alto):
        pivote = sublista[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if sublista[j] <= pivote:
                i += 1
                sublista[i], sublista[j] = sublista[j], sublista[i]
        sublista[i + 1], sublista[alto] = sublista[alto], sublista[i + 1]
        return i + 1

    if len(lista) > 1:
        _quicksort(lista, 0, len(lista) - 1)
    return lista

if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10]
    print("QuickSort - Original:", datos)
    print("QuickSort - Ordenado:", quick_sort(datos))
