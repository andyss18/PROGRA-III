import random
import time
import bisect

FILE_NAME = "numeros.txt"
N = 10_000_000
MIN = -50_000_000       
MAX = 50_000_000
BUSQUEDAS = 1000

# -------------------------------------
#  Generar archivo con 10M números
# -------------------------------------         
def generar_archivo():
    with open(FILE_NAME, "w") as f: 
        for _ in range(N):
            num = random.randint(MIN, MAX)
            f.write(str(num) + "\n")
    print("Archivo generado.")

# -------------------------------------
#  Cargar datos y crear estructuras
# -------------------------------------
def cargar_datos():     
    with open(FILE_NAME, "r") as f:
        datos = [int(line.strip()) for line in f]
    return datos

# -------------------------------------
#  Búsqueda en arreglo ordenado
# -------------------------------------
def buscar_binaria(arr, x):
    i = bisect.bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

# -------------------------------------
# Medición de rendimiento
# -------------------------------------
def medir_rendimiento(arr_ordenado, hash_set):
    tiempos_binaria = []
    tiempos_hash = []

    for _ in range(BUSQUEDAS):
        x = random.randint(MIN, MAX)

        # Arreglo ordenado
        inicio = time.perf_counter()
        buscar_binaria(arr_ordenado, x)
        fin = time.perf_counter()
        tiempos_binaria.append(fin - inicio)

        # Hash
        inicio = time.perf_counter()
        _ = x in hash_set
        fin = time.perf_counter()
        tiempos_hash.append(fin - inicio)

    return (
        sum(tiempos_binaria) / BUSQUEDAS,
        sum(tiempos_hash) / BUSQUEDAS
    )

# -------------------------------------
# MAIN
# -------------------------------------
def main():

    #generar_archivo()  # Ejecutar solo una vez

    print("Cargando datos...")
    datos = cargar_datos()

    print("Construyendo estructuras...")
    arr_ordenado = sorted(datos)
    hash_set = set(datos)

    print("Midiendo rendimiento...")
    tiempo_binaria, tiempo_hash = medir_rendimiento(arr_ordenado, hash_set)

    print("\nTabla Comparativa de Rendimiento")
    print("----------------------------------")
    print(f"Estructura           | Tiempo Promedio (seg)")
    print("----------------------------------")
    print(f"Arreglo Ordenado     | {tiempo_binaria:.10f}")
    print(f"Tabla Hash           | {tiempo_hash:.10f}")

    # Búsqueda manual
    while True:
        x = int(input("\nIngrese número a buscar (0 para salir): "))
        if x == 0:
            break

        print("Binaria:", buscar_binaria(arr_ordenado, x))
        print("Hash:", x in hash_set)

if __name__ == "__main__":
    main()