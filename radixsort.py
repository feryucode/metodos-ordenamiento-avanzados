def radix_sort(arr):
    if not arr:
        return []
    
    # Manejo de enteros (soporta positivos y negativos)
    enteros = [int(x) for x in arr]
    negativos = [-x for x in enteros if x < 0]
    positivos = [x for x in enteros if x >= 0]

    def _counting_sort_por_digito(nums, exp):
        n = len(nums)
        salida = [0] * n
        conteo = [0] * 10

        for num in nums:
            digito = (num // exp) % 10
            conteo[digito] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        for i in range(n - 1, -1, -1):
            digito = (nums[i] // exp) % 10
            salida[conteo[digito] - 1] = nums[i]
            conteo[digito] -= 1

        return salida

    def _ordenar_radix(nums):
        if not nums:
            return []
        max_num = max(nums)
        exp = 1
        resultado = nums.copy()
        while max_num // exp > 0:
            resultado = _counting_sort_por_digito(resultado, exp)
            exp *= 10
        return resultado

    neg_ord = _ordenar_radix(negativos)
    pos_ord = _ordenar_radix(positivos)

    # Invertir negativos para restaurar orden y devolver signo
    return [-x for x in reversed(neg_ord)] + pos_ord

if __name__ == "__main__":
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("RadixSort - Original:", datos)
    print("RadixSort - Ordenado:", radix_sort(datos))
