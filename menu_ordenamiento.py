from shellsort import shell_sort
from quicksort import quick_sort
from heapsort import heap_sort
from radixsort import radix_sort

def pedir_numeros():
    while True:
        try:
            n = int(input("\nIngrese la cantidad de números a ordenar: "))
            if n <= 0:
                print("Por favor, ingrese un número mayor a cero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    print(f"\nIngrese los {n} números.")
    print("(Puede escribirlos todos en una sola línea separados por espacios, o uno por uno):")
    
    numeros = []
    entrada = input("> ").strip()
    partes = entrada.split()
    
    if len(partes) == n:
        try:
            numeros = [float(x) if '.' in x else int(x) for x in partes]
            return numeros
        except ValueError:
            print("Uno de los valores ingresados no es un número válido. Ingréselos uno por uno:")
            numeros = []

    if not numeros:
        for i in range(n):
            while True:
                try:
                    val_str = input(f"Número {i + 1}: ").strip()
                    val = float(val_str) if '.' in val_str else int(val_str)
                    numeros.append(val)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
    return numeros

def menu_principal():
    while True:
        print("\n" + "=" * 45)
        print("     MENÚ DE MÉTODOS DE ORDENAMIENTO")
        print("=" * 45)
        print("1. ShellSort")
        print("2. QuickSort")
        print("3. HeapSort")
        print("4. Radix Sort")
        print("5. Salir")
        print("-" * 45)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!\n")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Elija un número del 1 al 5.")
            continue

        lista = pedir_numeros()
        print(f"\nLista original: {lista}")

        if opcion == "1":
            ordenada = shell_sort(lista)
            print(f"Lista ordenada con ShellSort: {ordenada}")
        elif opcion == "2":
            ordenada = quick_sort(lista)
            print(f"Lista ordenada con QuickSort: {ordenada}")
        elif opcion == "3":
            ordenada = heap_sort(lista)
            print(f"Lista ordenada con HeapSort: {ordenada}")
        elif opcion == "4":
            # Si hay números con decimales en Radix, avisar o redondear
            tiene_decimales = any(isinstance(x, float) and not x.is_integer() for x in lista)
            if tiene_decimales:
                print("\nNota: Radix Sort opera sobre dígitos enteros. Los valores fueron truncados a enteros.")
            ordenada = radix_sort([int(x) for x in lista])
            print(f"Lista ordenada con Radix Sort: {ordenada}")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
