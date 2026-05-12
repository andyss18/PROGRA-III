import re

def analizador_lexico():
    # El diccionario es nuestra Tabla Hash
    tabla_hash = {}
    lineas = []

    print("=== ANALIZADOR LÉXICO C++ ===")
    print("Escribe tu código abajo.")
    print("PARA FINALIZAR: Presiona ENTER dos veces seguidas.\n")

    # 1. Leer entrada línea por línea
    while True:
        entrada = input()
        if entrada == "": # Si el usuario da un enter vacío, se sale del bucle
            break
        lineas.append(entrada)

    # 2. Expresión regular para capturar los tokens requeridos
    # Busca palabras (identificadores/tipos), números y símbolos específicos
    patron = re.compile(r'([a-zA-Z_]\w*|\d+|==|!=|<=|>=|[+\-*/=;(),])')

    # 3. Procesar las líneas capturadas
    for num_fila, contenido_linea in enumerate(lineas):
        for coincidencia in patron.finditer(contenido_linea):
            token = coincidencia.group()
            num_columna = coincidencia.start()
            
            # Generar clave formato: fila,columna
            clave = f"{num_fila},{num_columna}"
            
            # Guardar en la Tabla Hash
            tabla_hash[clave] = token

    # 4. Mostrar resultados de forma estructurada
    if not tabla_hash:
        print("\nNo se ingresó ningún código.")
        return

    print("\n" + "="*30)
    print(f"{'CLAVE HASH':<15} | {'TOKEN':<10}")
    print("-" * 30)
    
    # Ordenamos las claves para que se vea bonito en la terminal
    for clave in sorted(tabla_hash.keys(), key=lambda x: [int(i) for i in x.split(',')]):
        print(f"{clave:<15} | {tabla_hash[clave]:<10}")
    print("="*30)

    # 5. Función de búsqueda (Requerimiento 7)
    print("\n--- Buscador de Tokens ---")
    while True:
        busqueda = input("Ingresa clave (fila,columna) para buscar o 'salir': ").strip()
        if busqueda.lower() == 'salir':
            break
        
        if busqueda in tabla_hash:
            print(f"-> Token encontrado: '{tabla_hash[busqueda]}'")
        else:
            print("-> Error: Esa clave no existe en la tabla.")

if __name__ == "__main__":
    analizador_lexico()