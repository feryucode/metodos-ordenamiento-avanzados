def shell_sort(arr):
    lista = arr.copy()
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista

if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90, 5]
    print("ShellSort - Original:", datos)
    print("ShellSort - Ordenado:", shell_sort(datos))
